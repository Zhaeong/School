module display_mux(done, done2, x1,y1,x2,y2, ,color, color2,color_out, en1,en2,en_out,x_out, y_out, crash, x_crash, y_crash, reset);
	input done, done2;
	input [7:0] x1,x2, x_crash;
	input [6:0] y1,y2, y_crash;
	input [2:0]color, color2;
	input en1,en2;
	input crash;
	input reset;
	
	reg en_on = 1'b1;
	
	output reg[7:0] x_out;
	output reg[6:0] y_out;
	output reg en_out;
	output reg[2:0] color_out;
	
	
	always @(*)
		begin
		
		if (!reset)
			begin 
			x_out <= x_crash;
			y_out <= y_crash;
			color_out <= 3'b111;
			end
		
		if(crash == 1'b1) 
			begin 
			x_out <= x_crash;
			y_out <= y_crash;
			color_out <= 3'b111;
			end
		else if (crash == 1'b0)
		begin
			if ((done == 1'b1) & (done2 == 1'b0))
				begin
				x_out <= x2;
				y_out <= y2;
				en_out <= en2;
				color_out <= color2;
				end
			else if ((done == 1'b0) & (done2 == 1'b1))
				begin
				x_out <= x1;
				y_out <= y1;
				en_out <= en1;
				color_out <= color;
				end		
		end
		
		end
	endmodule
