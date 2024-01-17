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
#include "lptim.h"
#include "tim.h"

//	┏┓  •  ┳
//	┃┓┏┓┓┏┓┃┏┓
//	┗┛┣┛┗┗┛┻┛┗
//	  ┛

struct GpioIn
{
	public:
		GpioIn(GPIO_TypeDef *gpio, uint16_t pin);
		GpioIn(GPIO_TypeDef *gpio, uint16_t pin, bool inv);

		bool read();

	private:
		GPIO_TypeDef *gpio;
		uint16_t pin;
		uint16_t inv;
};

//	┏┓  •  ┏┓
//	┃┓┏┓┓┏┓┃┃┓┏╋
//	┗┛┣┛┗┗┛┗┛┗┻┗
//	  ┛

struct GpioOut
{
	public:
		GpioOut(GPIO_TypeDef *gpio, uint16_t pin);
		GpioOut(GPIO_TypeDef *gpio, uint16_t pin, bool inv);

		void on();
		void off();
		void toggle();

	private:
		GPIO_TypeDef *gpio;
		uint16_t pin;
		uint16_t inv;
};


//	┏┓  •  ┳┳┓•
//	┃┓┏┓┓┏┓┃┃┃┓┏┏
//	┗┛┣┛┗┗┛┛ ┗┗┛┗
//	  ┛

#define PORT(LABEL) LABEL##_GPIO_Port
#define PIN(LABEL) LABEL##Pin

//	┏┓      ┓
//	┣ ┏┓┏┏┓┏┫┏┓┏┓
//	┗┛┛┗┗┗┛┗┻┗ ┛
//

struct Encoder
{
	public:
		Encoder(LPTIM_TypeDef *lptim, float ratio);
		Encoder(LPTIM_TypeDef *lptim, float gear_ratio, float encoder_ratio);

		float getAngleSpeed();

	private:
		LPTIM_TypeDef *lptim;
		float ratio;
};

//	┏┓      ┏┓
//	┃┃┓┏┏┏┳┓┃┃┓┏╋
//	┣┛┗┻┛┛┗┗┗┛┗┻┗
//

enum struct PwmOutCh : uint32_t
{
	_1,
	_2,
	_3,
	_4,
	_5,
	_6
};

struct PwmOut
{
	public:
		PwmOut(TIM_TypeDef *tim, PwmOutCh channel);

		void setDuty(float duty);
	private:
		TIM_TypeDef *tim;
		__IO uint32_t TIM_TypeDef::*channel_cmp_reg;
};

#endif /* INC_COMMON_HPP_ */
