/*
 * common.hpp
 *
 *  Created on: Jan 12, 2024
 *      Author: Piotr Lesicki
 */

#ifndef INC_COMMON_HPP_
#define INC_COMMON_HPP_

#include "main.h"
#include "gpio.h"

//	┏┓  •  ┳
//	┃┓┏┓┓┏┓┃┏┓
//	┗┛┣┛┗┗┛┻┛┗
//	  ┛

struct GpioIn
{
	GpioIn(GPIO_Typedef *gpio, uint16_t pin);
	GpioIn(GPIO_Typedef *gpio, uint16_t pin, bool inv);

	bool read();

	GPIO_Typedef *gpio;
	uint16_t pin;
	uint16_t inv;
};

//	┏┓  •  ┏┓
//	┃┓┏┓┓┏┓┃┃┓┏╋
//	┗┛┣┛┗┗┛┗┛┗┻┗
//	  ┛

struct GpioOut
{
	GpioOut(GPIO_Typedef *gpio, uint16_t pin);
	GpioOut(GPIO_Typedef *gpio, uint16_t pin, bool inv);

	void on();
	void off();
	void toggle();

	GPIO_Typedef *gpio;
	uint16_t pin;
	uint16_t inv;
};

#define PORT(LABEL) LABEL##_GPIO_Port
#define PIN(LABEL) LABEL##Pin

#endif /* INC_COMMON_HPP_ */
