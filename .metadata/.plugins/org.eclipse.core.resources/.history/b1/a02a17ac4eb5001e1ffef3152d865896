/*
 * spi_api.cpp
 *
 *  Created on: Jan 13, 2024
 *      Author: Piotr Lesicki
 */

#include <queue_peek.h>
#include "spi_api.hpp"

#include "tx_api.h"
#include "spi.h"
#include <cstring>

//	┏┓  •┳┓     ┳┓          ┓┏     ┓┓
//	┗┓┏┓┓┃┃┏┳┓┏┓┣┫┏┓┏┓┓┏┏┓┏╋┣┫┏┓┏┓┏┫┃┏┓┏┓
//	┗┛┣┛┗┻┛┛┗┗┗┻┛┗┗ ┗┫┗┻┗ ┛┗┛┗┗┻┛┗┗┻┗┗ ┛
//	  ┛              ┗

class SpiDmaRequestHandler
{
	public:
		SpiDmaRequestHandler() = delete;
		SpiDmaRequestHandler(const SpiDmaRequestHandler&) = delete;
		SpiDmaRequestHandler& operator=(SpiDmaRequestHandler const&) = delete;

		constexpr static void putRequest(SpiDmaRequest &request)
		{
			tx_queue_send(&SpiDmaRequestHandler::queue, &request, TX_NO_WAIT);
		}
		constexpr static void peekRequest(SpiDmaRequest &request)
		{
			queue_peek(&SpiDmaRequestHandler::queue, &request, TX_NO_WAIT);
		}
		constexpr static void getRequest(SpiDmaRequest &request)
		{
			tx_queue_receive(&SpiDmaRequestHandler::queue, &request, TX_NO_WAIT);
		}
		constexpr static uint32_t requestCount()
		{
			return SpiDmaRequestHandler::queue.tx_queue_enqueued;
		}

	private:
		static inline TX_QUEUE queue;
		static inline uint8_t queue_data[sizeof(SpiDmaRequest) * 8];
		static inline char queue_name[16] = "SpiDmaReqHandle";

		static inline uint32_t queue_creation_status = tx_queue_create(&SpiDmaRequestHandler::queue, SpiDmaRequestHandler::queue_name, sizeof(SpiDmaRequest), SpiDmaRequestHandler::queue_data, sizeof(SpiDmaRequestHandler::queue_data));
};

//	┏┓  •┳┓     ┳┓
//	┗┓┏┓┓┃┃┏┳┓┏┓┣┫┏┓┏┓┓┏┏┓┏╋
//	┗┛┣┛┗┻┛┛┗┗┗┻┛┗┗ ┗┫┗┻┗ ┛┗
//	  ┛              ┗

SpiDmaRequest::SpiDmaRequest(uint8_t *rx_data, uint8_t *tx_data, size_t size, GpioOut *cs, std::atomic<bool> *pending_request) : rx_data(rx_data), tx_data(tx_data), size(size), cs(cs), pending_request(pending_request) { }

void SpiDmaRequest::send()
{
	this->pending_request->store(true);
	if(hspi1.State == HAL_SPI_STATE_READY)
	{
		this->cs->on();
		HAL_SPI_TransmitReceive_DMA(&hspi1, this->tx_data, this->rx_data, this->size);
	}
	SpiDmaRequestHandler::putRequest(*this);
}

//	┳
//	┃┏┓╋┏┓┏┓┏┓┓┏┏┓╋
//	┻┛┗┗┗ ┛ ┛ ┗┻┣┛┗
//				┛

void HAL_SPI_TxRxCpltCallback(SPI_HandleTypeDef *hspi)
{
	SpiDmaRequest request_buff { nullptr, nullptr, 0, nullptr, nullptr };
	SpiDmaRequestHandler::peekRequest(request_buff);
	request_buff.cs->off();
	request_buff.pending_request->store(false);
	if(SpiDmaRequestHandler::requestCount() != TX_NO_MESSAGES)
	{
		SpiDmaRequestHandler::getRequest(request_buff);
		request_buff.cs->on();
	}
}
