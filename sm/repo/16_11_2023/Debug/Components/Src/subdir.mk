################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Components/Src/bmp2.c \
../Components/Src/bmp2_config.c \
../Components/Src/dio.c \
../Components/Src/heater.c \
../Components/Src/heater_config.c \
../Components/Src/pwm.c 

OBJS += \
./Components/Src/bmp2.o \
./Components/Src/bmp2_config.o \
./Components/Src/dio.o \
./Components/Src/heater.o \
./Components/Src/heater_config.o \
./Components/Src/pwm.o 

C_DEPS += \
./Components/Src/bmp2.d \
./Components/Src/bmp2_config.d \
./Components/Src/dio.d \
./Components/Src/heater.d \
./Components/Src/heater_config.d \
./Components/Src/pwm.d 


# Each subdirectory must supply rules for building sources it contributes
Components/Src/%.o Components/Src/%.su Components/Src/%.cyclo: ../Components/Src/%.c Components/Src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"C:/Users/HP/Desktop/studia/sm/repo/16_11_2023/Components/Inc" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Components-2f-Src

clean-Components-2f-Src:
	-$(RM) ./Components/Src/bmp2.cyclo ./Components/Src/bmp2.d ./Components/Src/bmp2.o ./Components/Src/bmp2.su ./Components/Src/bmp2_config.cyclo ./Components/Src/bmp2_config.d ./Components/Src/bmp2_config.o ./Components/Src/bmp2_config.su ./Components/Src/dio.cyclo ./Components/Src/dio.d ./Components/Src/dio.o ./Components/Src/dio.su ./Components/Src/heater.cyclo ./Components/Src/heater.d ./Components/Src/heater.o ./Components/Src/heater.su ./Components/Src/heater_config.cyclo ./Components/Src/heater_config.d ./Components/Src/heater_config.o ./Components/Src/heater_config.su ./Components/Src/pwm.cyclo ./Components/Src/pwm.d ./Components/Src/pwm.o ./Components/Src/pwm.su

.PHONY: clean-Components-2f-Src

