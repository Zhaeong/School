module reset_display(clock, x_out, y_out, reset);

input clock;
input reset;

output reg [7:0]x_out;
output reg [6:0]y_out;




always @(posedge clock)
	if(~reset) begin
		x_out <= 8'b0;
		y_out <= 7'b0;
	end
	
	else begin
		x_out <= x_out + 1;
		
		if (x_out == 8'd159) begin
			x_out <= 0;
			y_out <= y_out + 1;
		end
		
		if (y_out == 7'd119)
			y_out <= 0;
	end
	
endmodule
