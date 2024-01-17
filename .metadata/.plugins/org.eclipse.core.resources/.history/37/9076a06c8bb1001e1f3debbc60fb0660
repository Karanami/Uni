/*
 * common.cpp
 *
 *  Created on: Jan 12, 2024
 *      Author: Piotr Lesicki
 */


#include "common.hpp"

//	┏┓  •  ┳
//	┃┓┏┓┓┏┓┃┏┓
//	┗┛┣┛┗┗┛┻┛┗
//	  ┛

GpioIn::GpioIn(GPIO_Typedef *gpio, uint16_t pin) : gpio(gpio), pin(pin), inv(0) { }

GpioIn::GpioIn(GPIO_Typedef *gpio, uint16_t pin, bool inv) : gpio(gpio), pin(pin), inv(inv ? pin : 0) { }

inline bool GpioIn::read()
{
	return bool(gpio->IDR & pin ^ inv);
}

//	┏┓  •  ┏┓   
//	┃┓┏┓┓┏┓┃┃┓┏╋
//	┗┛┣┛┗┗┛┗┛┗┻┗
//	  ┛         

GpioOut::GpioOut(GPIO_Typedef *gpio, uint16_t pin) : gpio(gpio), pin(pin), inv(0) { }

GpioOut::GpioOut(GPIO_Typedef *gpio, uint16_t pin, bool inv) : gpio(gpio), pin(pin), inv(inv ? pin : 0) { }

inline void GpioOut::on()
{
	gpio->ODR = gpio->ODR & ~inv | (pin ^ inv);
}

inline void GpioOut::off()
{
	gpio->ODR = gpio->ODR & ~(pin ^ inv) | inv;
}

inline void GpioOut::toggle()
{
	gpio->ODR ^= pin;
}
