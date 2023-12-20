/**
  ******************************************************************************
  * @file     : dio.c
  * @author   : AW    Adrian.Wojcik@put.poznan.pl
  * @version  : 1.3.0
  * @date     : Nov 27, 2022
  * @brief    : Digital inputs/outputs components driver.
  *
  ******************************************************************************
  */

/* Private includes ----------------------------------------------------------*/
#include "dio.h"

/* Private typedef -----------------------------------------------------------*/

/* Private define ------------------------------------------------------------*/

/* Private macro -------------------------------------------------------------*/

/* Private variables ---------------------------------------------------------*/

/* Public variables ----------------------------------------------------------*/

/* Private function prototypes -----------------------------------------------*/

/* Public function prototypes ------------------------------------------------*/

/* Private functions ---------------------------------------------------------*/

/* Public functions ----------------------------------------------------------*/
/**
 * @brief Resets digital output (writes '0')
 * @param[in] hdio  : Digital I/O handler
 * @retval None
 */
void DIO_WriteLow(DIO_Handle_TypeDef* hdio)
{
  hdio->State = GPIO_PIN_RESET;
  HAL_GPIO_WritePin(hdio->Port, hdio->Pin, hdio->State);
}

/**
 * @brief Sets digital output (writes '1')
 * @param[in] hdio  : Digital I/O handler
 * @retval None
 */
void DIO_WriteHigh(DIO_Handle_TypeDef* hdio)
{
  hdio->State = GPIO_PIN_SET;
  HAL_GPIO_WritePin(hdio->Port, hdio->Pin, hdio->State);
}

/**
 * @brief Writes gieven state to digital output
 * @param[in] hdio  : Digital I/O handler
 * @param[in] state : Digital output state (0 or 1)
 * @retval None
 */
void DIO_Write(DIO_Handle_TypeDef* hdio, _Bool state)
{
  hdio->State = state;
  HAL_GPIO_WritePin(hdio->Port, hdio->Pin, hdio->State);
}

/**
 * @brief Toggles digital output ('0' to '1' or '1' to '0')
 * @param[in] hdio  : Digital I/O handler
 * @retval None
 */
void DIO_Toggle(DIO_Handle_TypeDef* hdio)
{
  hdio->State ^= 1;
  HAL_GPIO_TogglePin(hdio->Port, hdio->Pin);
}

/**
 * @brief Reads digital input
 * @param[in] hdio  : Digital I/O handler
 * @retval Input state (0 or 1)
 */
_Bool DIO_Read(const DIO_Handle_TypeDef* hdio)
{
  return (_Bool)HAL_GPIO_ReadPin(hdio->Port, hdio->Pin);
}
