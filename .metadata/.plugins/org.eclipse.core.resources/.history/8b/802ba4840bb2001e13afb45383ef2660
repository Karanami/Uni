/*
 * max11643.cpp
 *
 *  Created on: Jan 13, 2024
 *      Author: Piotr Lesicki
 */


#include <max11643.hpp>

Max11643::Max11643(SPI_HandleTypedef *hspi, GpioOut *cs, GpioIn *it) : hspi(hspi), cs(cs), it(it), data({ 0 }), pending_req(false) { };

void Max11643::requestData()
{

}

bool Max11643::canRequest()
{
	if (pending_req) return false;
	return it->read();
}

inline uint8_t Max11643::getChannelAdc(uint32_t channel)
{
	return this->data[channel];
}
