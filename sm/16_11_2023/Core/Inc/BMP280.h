/*
 * BMP280.h
 *
 *  Created on: Nov 16, 2023
 *      Author: HP
 */

#ifndef INC_BMP280_H_
#define INC_BMP280_H_

#include "spi.h"

# define BMP2_SPI_BUFFER_LEN 28 //! @see BMP280 technical note p. 24
# define BMP2_DATA_INDEX 1 //! @see BMP280 technical note p. 31 -32
# define BMP2_REG_ADDR_INDEX 0 //! @see BMP280 technical note p. 31 -32
# define BMP2_REG_ADDR_LEN 1 //! @see BMP280 technical note p. 31 -32

#define BMP2_BIT_TO_PA 2.62f
#define BMP2_BIT_TO_T 0.0050f

#define BMP2_SPI &hspi4

#define BMP2_ctrl_meas 0xF4
#define BMP2_config 0xF5
#define BMP2_temp_msb 0xFA
#define BMP2_press_msb 0xF7

#define BMP2_osrs_p 0b001
#define BMP2_osrs_t 0b001
#define BMP2_mode 0b00000011


void bmp280Write(uint8_t reg_addr , const uint8_t * reg_data , uint32_t length);
void bmp280Read(uint8_t reg_addr , const uint8_t * reg_data , uint32_t length);
void bmp280Init();

#endif /* INC_BMP280_H_ */
