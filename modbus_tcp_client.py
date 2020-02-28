import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md

# 远程连接到服务器端
master = mt.TcpMaster("127.0.0.1", 9999)
master.set_timeout(5.0)

# @slave=1 : identifier of the slave. from 1 to 247.  0为广播所有的slave
# @function_code=READ_HOLDING_REGISTERS：功能码
# @starting_address=1：开始地址
# @quantity_of_x=3：寄存器/线圈的数量
# @output_value：一个整数或可迭代的值：1/[1,1,1,0,0,1]/xrange(12)
# @data_format
# @expected_length
Hold_value = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=1, quantity_of_x=3, output_value=5)
Hold_value = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=1, quantity_of_x=3, output_value=5)
Coils_value = master.execute(slave=1, function_code=md.READ_COILS, starting_address=1,  quantity_of_x=3, output_value=5)

print(Hold_value)  # 取到的寄存器的值格式为元组(55, 12, 44)
print(Hold_value)  # 取到的寄存器的值格式为元组(1, 1, 1)