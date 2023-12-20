/*
 * BH1750.h
 *
 *  Created on: Nov 8, 2023
 *      Author: user
 */

#ifndef INC_BH1750_H_
#define INC_BH1750_H_

#include "i2c.h"

void bh1750Init(I2C_HandleTypeDef* hi2c);

float bh1750GetMes(I2C_HandleTypeDef* hi2c);

#endif /* INC_BH1750_H_ */
