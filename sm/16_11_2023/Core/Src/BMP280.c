/*
 * BMP280.c
 *
 *  Created on: Nov 16, 2023
 *      Author: HP
 */


#include "BMP280.h"
#include "gpio.h"

void bmp280Write(uint8_t reg_addr , const uint8_t * reg_data , uint32_t length)
{
    /* Software slave selection procedure */
    HAL_GPIO_WritePin ( SPI4_CS_GPIO_Port, SPI4_CS_Pin , GPIO_PIN_RESET ) ;

    /* Data exchange */
    HAL_SPI_Transmit ( BMP2_SPI , &reg_addr , BMP2_REG_ADDR_LEN , 100 ) ;
    HAL_SPI_Transmit ( BMP2_SPI , reg_data , length , 100 ) ;

    /* Disable all slaves */
    HAL_GPIO_WritePin ( SPI4_CS_GPIO_Port, SPI4_CS_Pin , GPIO_PIN_SET ) ;
}

void bmp280Read(uint8_t reg_addr , const uint8_t * reg_data , uint32_t length)
{
    /* Software slave selection procedure */
    HAL_GPIO_WritePin ( SPI4_CS_GPIO_Port, SPI4_CS_Pin , GPIO_PIN_RESET ) ;
    reg_addr |= 0b10000000;

    /* Data exchange */
    HAL_SPI_Transmit ( BMP2_SPI , &reg_addr , BMP2_REG_ADDR_LEN , 100 ) ;
    HAL_SPI_Receive ( BMP2_SPI , reg_data , length , 100 ) ;

    /* Disable all slaves */
    HAL_GPIO_WritePin ( SPI4_CS_GPIO_Port, SPI4_CS_Pin , GPIO_PIN_SET ) ;
}

typedef struct
{
	uint8_t mode : 2;
	uint8_t osrs_p : 3;
	uint8_t osrs_t : 3;
}Bmp280Config;

void bmp280Init()
{
	Bmp280Config config =
	{
		.osrs_t = BMP2_osrs_t,
		.osrs_p = BMP2_osrs_p,
		.mode = BMP2_mode
	};
	uint8_t buff;
	memcpy(&buff, &config, 1);
	bmp280Write(BMP2_ctrl_meas, &config, 1);
}
