#include "BH1750.h"

void bh1750Init(I2C_HandleTypeDef* hi2c)
{
	uint8_t temp;
	temp = 0b1; //power on
	HAL_I2C_Master_Transmit(hi2c, (0x23 << 1), &temp, 1, 100);
	temp = 0b10000; //con h-res
	HAL_I2C_Master_Transmit(hi2c, (0x23 << 1), &temp, 1, 100);
	HAL_Delay(240);
}

float bh1750GetMes(I2C_HandleTypeDef* hi2c)
{
	const float k = 1 / 1.2;
	uint8_t temp[2];
	HAL_I2C_Master_Receive(hi2c, (0x23 << 1) , temp, 2, 100);
	uint16_t mes = ((uint16_t)(temp[0]) << 8) + (uint16_t)(temp[1]);
	float lux = (float)(mes) * 1000 * k;

	return lux;
}

