module display_heli(clock, x, y, out_x, out_y, color, done, en,start);
	input clock;
	input [7:0]x;
	input [6:0]y;
	input start;
	output reg en;
	output reg[7:0] out_x;
	output reg[6:0] out_y;
	output reg[2:0] color;
	
	reg [4:0]d;
	output reg done;
	
	always @(posedge clock)
		if (d == 5'b00000)
			begin
			en = 1'b1;
			out_x <= x - 3;
			out_y <= y - 2;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d == 5'b00001)
			begin
			en = 1'b1;
			out_x <= x - 1;
			out_y <= y - 3;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b00010)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y - 3;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b00011)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y - 3;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b00100)
			begin
			en = 1'b1;
			out_x <= x - 1;
			out_y <= y - 2;
			color <= 3'b000;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b00101)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y - 2;
			color <= 3'b000;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b00110)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y - 2;
			color <= 3'b000;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b00111)
			begin
			en = 1'b1;
			out_x <= x - 3;
			out_y <= y - 1;
			color <= 3'b000;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b01000)
			begin
			en = 1'b1;
			out_x <= x - 2;
			out_y <= y - 1;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b01001)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y - 1;
			color <= 3'b001;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b01010)
			begin
			en = 1'b1;
			out_x <= x-3;
			out_y <= y;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b01011)
			begin
			en = 1'b1;
			out_x <= x-2;
			out_y <= y;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b01100)
			begin
			en = 1'b1;
			out_x <= x-1;
			out_y <= y;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b01101)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b01110)
			begin
			en = 1'b1;
			out_x <= x+1;
			out_y <= y;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b01111)
			begin
			en = 1'b1;
			out_x <= x-3;
			out_y <= y+1;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b10000)
			begin
			en = 1'b1;
			out_x <= x-2;
			out_y <= y+1;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b10001)
			begin
			en = 1'b1;
			out_x <= x-1;
			out_y <= y+1;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b10010)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y+1;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b10011)
			begin
			en = 1'b1;
			out_x <= x+1;
			out_y <= y+1;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b10100)
			begin
			en = 1'b1;
			out_x <= x-1;
			out_y <= y+2;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b10101)
			begin
			en = 1'b1;
			out_x <= x-1;
			out_y <= y+2;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b10110)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y+2;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==5'b10111)
			begin
			en = 1'b1;
			out_x <= x+1;
			out_y <= y+2;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		//endstate
		else if (d==5'b11000)
			begin
			en = 1'b0;
			done <= 1'b1;
			if (start == 1)  
				begin
				d <= 5'b00000;
				end
			end
endmodule

