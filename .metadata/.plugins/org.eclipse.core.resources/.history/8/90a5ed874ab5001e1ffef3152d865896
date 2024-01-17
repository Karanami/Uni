/*
 * common.cpp
 *
 *  Created on: Jan 12, 2024
 *      Author: Piotr Lesicki
 */


#include "common.hpp"
#include <algorithm>
#include <stm32wbxx_ll_lptim.h>

//	┏┓  •  ┳
//	┃┓┏┓┓┏┓┃┏┓
//	┗┛┣┛┗┗┛┻┛┗
//	  ┛

GpioIn::GpioIn(GPIO_TypeDef *gpio, uint16_t pin) : gpio(gpio), pin(pin), inv(0) { }

GpioIn::GpioIn(GPIO_TypeDef *gpio, uint16_t pin, bool inv) : gpio(gpio), pin(pin), inv(inv ? pin : 0) { }

inline bool GpioIn::read()
{
	return bool((gpio->IDR & pin) ^ inv);
}

//	┏┓  •  ┏┓   
//	┃┓┏┓┓┏┓┃┃┓┏╋
//	┗┛┣┛┗┗┛┗┛┗┻┗
//	  ┛         

GpioOut::GpioOut(GPIO_TypeDef *gpio, uint16_t pin) : gpio(gpio), pin(pin), inv(0) { }

GpioOut::GpioOut(GPIO_TypeDef *gpio, uint16_t pin, bool inv) : gpio(gpio), pin(pin), inv(inv ? pin : 0) { }

inline void GpioOut::on()
{
	gpio->ODR = (gpio->ODR & ~inv) | (pin ^ inv);
}

inline void GpioOut::off()
{
	gpio->ODR = (gpio->ODR & ~(pin ^ inv)) | inv;
}

inline void GpioOut::toggle()
{
	gpio->ODR ^= pin;
}

//	┏┓      ┓
//	┣ ┏┓┏┏┓┏┫┏┓┏┓
//	┗┛┛┗┗┗┛┗┻┗ ┛
//

Encoder::Encoder(LPTIM_TypeDef *lptim, float ratio) : lptim(lptim), ratio(ratio)
{
	LL_LPTIM_EnableResetAfterRead(lptim);
}

Encoder::Encoder(LPTIM_TypeDef *lptim, float gear_ratio, float encoder_ratio) : lptim(lptim), ratio(gear_ratio * encoder_ratio)
{
	LL_LPTIM_EnableResetAfterRead(lptim);
}

inline float Encoder::getAngleSpeed()
{
	return float(LL_LPTIM_GetCounter(this->lptim)) * ratio;
}

//	┏┓      ┏┓
//	┃┃┓┏┏┏┳┓┃┃┓┏╋
//	┣┛┗┻┛┛┗┗┗┛┗┻┗
//

PwmOut::PwmOut(TIM_TypeDef *tim, PwmOutCh channel) : tim(tim)
{
	switch (channel)
	{
	case PwmOutCh::_1:
		this->channel_cmp_reg = &TIM_TypeDef::CCR1;
		break;
	case PwmOutCh::_2:
		this->channel_cmp_reg = &TIM_TypeDef::CCR2;
		break;
	case PwmOutCh::_3:
		this->channel_cmp_reg = &TIM_TypeDef::CCR3;
		break;
	case PwmOutCh::_4:
		this->channel_cmp_reg = &TIM_TypeDef::CCR4;
		break;
	case PwmOutCh::_5:
		this->channel_cmp_reg = &TIM_TypeDef::CCR5;
		break;
	case PwmOutCh::_6:
		this->channel_cmp_reg = &TIM_TypeDef::CCR6;
		break;
	}
}

void PwmOut::setDuty(float duty)
{
	duty = std::clamp(duty, 0.f, 100.f);
	uint32_t cmp = uint32_t(float(LL_TIM_GetAutoReload(tim)) * duty);
	//LL_TIM_OC_SetCompareCH1(TIMx, CompareValue)
	tim->*channel_cmp_reg = cmp;
}
