/*
 * spi_api.hpp
 *
 *  Created on: Jan 13, 2024
 *      Author: Piotr Lesicki
 */

#ifndef INC_SPI_API_HPP_
#define INC_SPI_API_HPP_

#include "main.h"
#include "common.hpp"

#include <atomic>

struct SpiDmaRequest
{
	explicit SpiDmaRequest(uint8_t *rx_data, uint8_t *tx_data, size_t size, GpioOut *cs, std::atomic<bool> *pending_request);

	void send();

	uint8_t *rx_data;
	uint8_t *tx_data;
	size_t size;
	GpioOut *cs;
	std::atomic<bool> *pending_request;
};

#endif /* INC_SPI_API_HPP_ */
