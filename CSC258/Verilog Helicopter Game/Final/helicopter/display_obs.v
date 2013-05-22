module display_obs(clock, x, y, out_x, out_y, color, done, en,start);
	input clock;
	input [7:0]x;
	input [6:0]y;
	input start;
	output reg en;
	output reg[7:0] out_x;
	output reg[6:0] out_y;
	output reg[2:0] color;
	
	reg [5:0]d = 6'b000000;
	output reg done;
	
	always @(posedge clock)
		if (d == 6'b000000)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y - 2;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d == 6'b000001)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y - 1;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b000010)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b000011)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y + 1;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b000100)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y + 2;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b000101)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y + 3;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b000110)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y + 4;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b000111)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y + 5;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b001000)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y - 2;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b001001)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y - 1;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		
		else if (d ==6'b001010)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b001011)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y + 1;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b001100)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y + 2;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b001101)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y + 3;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b001110)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y + 4;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b001111)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y + 5;
			color <= 3'b100;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b010000)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y + 6;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b010001)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y + 6;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b010010)
			begin
			en = 1'b1;
			out_x <= x;
			out_y <= y - 3;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b010011)
			begin
			en = 1'b1;
			out_x <= x + 1;
			out_y <= y - 3;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b010100)
			begin
			en = 1'b1;
			out_x <= x + 2;
			out_y <= y - 3;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end	
		else if (d ==6'b010101)
			begin
			en = 1'b1;
			out_x <= x + 2;
			out_y <= y - 2;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b010110)
			begin
			en = 1'b1;
			out_x <= x + 2;
			out_y <= y - 1;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b010111)
			begin
			en = 1'b1;
			out_x <= x + 2;
			out_y <= y;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b011000)
			begin
			en = 1'b1;
			out_x <= x + 2;
			out_y <= y + 1;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b011001)
			begin
			en = 1'b1;
			out_x <= x + 2;
			out_y <= y + 2;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b011010)
			begin
			en = 1'b1;
			out_x <= x + 2;
			out_y <= y + 3;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b011011)
			begin
			en = 1'b1;
			out_x <= x + 2;
			out_y <= y + 4;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b011100)
			begin
			en = 1'b1;
			out_x <= x + 2;
			out_y <= y + 5;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		else if (d ==6'b011101)
			begin
			en = 1'b1;
			out_x <= x + 2;
			out_y <= y + 6;
			color <= 3'b111;
			d <= d + 1;
			done <= 1'b0;
			end
		//break

		else if (d==6'b011110)
			begin
			en = 1'b0;
			done <= 1'b1;
			if (start == 1)  
				begin
				d <= 6'b000000;
				end
			end
endmodule

