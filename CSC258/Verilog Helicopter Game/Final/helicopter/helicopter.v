module helicopter(CLOCK_50, SW, KEY,VGA_R, VGA_G, VGA_B,VGA_HS, VGA_VS, VGA_BLANK ,VGA_SYNC, VGA_CLK,HEX0,HEX1,HEX2,HEX3);
	input CLOCK_50;
	input [3:0] KEY;
	input [17:0] SW;
	output [9:0] VGA_R, VGA_G, VGA_B; //for vga module.
	output VGA_HS, VGA_VS, VGA_BLANK, VGA_SYNC, VGA_CLK; //for vga module.
	
	output [0:6]HEX0,HEX1,HEX2,HEX3;
	
	
	wire [7:0] X, X2, X_final;
	wire [6:0] Y, Y2, Y_final;
	
	reg [7:0] X_temp, X_temp2, X_temp3;
	reg [6:0] Y_temp, Y_temp2, Y_temp3;
	
	wire en, en2, en_final;
	wire reset = ~SW[17];
	
	//hex counter
	reg [3:0] hexcounter, hexcounter2,hexcounter3,hexcounter4;
	
	reg start;
	reg start2;
	wire [2:0]color, color2, color_final;

	//slowed down clock
	reg c;
	reg c2;
	reg c3;
	
	//collision detection for crashes
	reg crash;
	
	
	integer counter = 0;
	integer counter2 = 0;
	integer counter3 =0;
	
	wire done;
	
	//heli clock
	always @(posedge CLOCK_50)
		begin

		counter = counter + 1 ;
		if (counter == 500000)
			begin
				c <= c+1'b1 ;
				counter = 0;
				start = 1'b1;
			end
		else if (counter == 499999)
			start = 1'b1;
		end

	//obstacle clock
	always @(posedge CLOCK_50)
		begin
		counter2 = counter2 + 1 ;
		if (counter2 == 200011)
			begin
				c2 <= c2+1'b1 ;
				counter2 = 0;
				start2 = 1'b1;
			end
		else if (counter2 == 200010)
			start2 = 1'b1;
		end
		
	//hex clock
	always @(posedge CLOCK_50)
		begin
		if (crash == 1'b0)
			counter3 = counter3 + 1 ;
		if (counter3 == 5000000)
			begin
				c3 <= c3+1'b1 ;
				counter3 = 0;
			end
		end
		
	
	
	always @(posedge c3)
		if(~SW[0]) begin
			hexcounter <= 4'b0;
			hexcounter2 <= 4'b0;
			hexcounter3 <= 4'b0;
			hexcounter4 <= 4'b0;
		end
		
		else begin
			hexcounter <= hexcounter + 1;
			if (hexcounter == 4'b1001) 
				begin
				hexcounter <= 0;
				hexcounter2 <= hexcounter2 + 1;
				end
			
			if ((hexcounter2 == 4'b1001) & (hexcounter == 4'b1001))
				begin
				hexcounter2 <= 0;
				hexcounter3 <= hexcounter3 + 1;
				end
			if ((hexcounter3 == 4'b1001) & (hexcounter2 == 4'b1001)& (hexcounter == 4'b1001))
				begin
				hexcounter3 <= 0;
				hexcounter4 <= hexcounter4 + 1;
				end
			if ((hexcounter4 == 4'b1001)&(hexcounter3 == 4'b1001) & (hexcounter2 == 4'b1001)& (hexcounter == 4'b1001))
				begin
				hexcounter <=0;
				hexcounter2 <= 0;
				hexcounter3 <= 0;
				hexcounter4 <= 0;
				end
		end
	
	hex_decoder h1 (hexcounter, HEX0);
	hex_decoder h2 (hexcounter2, HEX1);
	hex_decoder h3 (hexcounter3, HEX2);
	hex_decoder h4 (hexcounter4, HEX3);
	
	
	
	
	//heli fsm
	always @(posedge c)
		begin
		if (!SW[0]) 
			begin // reset state
			X_temp = 8'b00001111;
			Y_temp = 7'b0111110;
			crash = 1'b0;
			end
		if (crash == 1'b0)
		begin
			if (KEY[3]) // down
			begin
			if(Y_temp + 1'b1 != 7'b1110000)
				begin
				Y_temp = Y_temp + 1'b1;
				
				if ((X_temp2 == 8'b00001111) ||(X_temp2 == 8'b00010000))
					begin
					if (Y_temp == Y_temp2)
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 - 1))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 - 2))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 - 3))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 + 1))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 + 2))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 + 3))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 + 4))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 + 5))
						crash <= 1'b1;
					else if ((Y_temp-2)==(Y_temp2 +5 ))
						crash <= 1'b1;
					end
				end
				
			else if (Y_temp + 1'b1 == 7'b1110000)
				crash <= 1'b1;
				
			end
		else if (!KEY[3]) // up
			begin
			if(Y_temp - 1'b1 != 7'b0000010)
				begin
				Y_temp = Y_temp - 1'b1;
				
				if ((X_temp2 == 8'b00001111) ||(X_temp2 == 8'b00010000))
					begin
					if (Y_temp == Y_temp2)
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 - 1))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 - 2))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 - 3))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 + 1))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 + 2))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 + 3))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 + 4))
						crash <= 1'b1;
					else if (Y_temp == (Y_temp2 + 5))
						crash <= 1'b1;
					else if ((Y_temp-2)==(Y_temp2 +5 ))
						crash <= 1'b1;
				end
			end
			
			else if (Y_temp - 1'b1 == 7'b0000010)
				crash <= 1'b1;
			
		end
		end
		end
	
	//obstacle fsm
	always @(posedge c2)
		begin
		if (!SW[0]) 
			begin // reset state
			X_temp2 = 8'b10011011;
			Y_temp2 = 7'b0111110;
			end
		else // left
			begin
			X_temp2 = X_temp2 - 1'b1;
			if (X_temp2 == (8'b0 - 8'b11)) 
				begin
				X_temp2 = 8'b10011011;
				end
			if (!KEY[0]) 
				begin
				if(Y_temp2 + 1'b1 != 7'b1110000)
					Y_temp2 = Y_temp2 + 1'b1;
				end
			else if (!KEY[1])
				begin
				if(Y_temp2 - 1'b1 != 7'b0000010)
					Y_temp2 = Y_temp2 - 1'b1;
				end
			end

		end
			
	
	display_heli d0 (CLOCK_50, X_temp, Y_temp, X, Y, color, done, en, start);
	
	display_obs d1 (CLOCK_50, X_temp2, Y_temp2, X2, Y2, color2, done2, en2, start2);
	
	reset_display d2(CLOCK_50, X_temp3,Y_temp3, SW[0]);
	
	display_mux m0 (done, done2, X, Y, X2, Y2,color, color2, color_final, en, en2, en_final, X_final, Y_final, crash, X_temp3, Y_temp3, SW[0]);
	
	
		vga_adapter VGA(
				.resetn(reset),
				.clock(CLOCK_50),
				.colour(color_final),
				.x(X_final),
				.y(Y_final),
				.plot(en_final),
				/* Signals for the DAC to drive the monitor. */
				.VGA_R(VGA_R),
				.VGA_G(VGA_G),
				.VGA_B(VGA_B),
				.VGA_HS(VGA_HS),
				.VGA_VS(VGA_VS),
				.VGA_BLANK(VGA_BLANK),
				.VGA_SYNC(VGA_SYNC),
				.VGA_CLK(VGA_CLK));
				defparam VGA.RESOLUTION = "160x120";
				defparam VGA.MONOCHROME = "FALSE";
				defparam VGA.BITS_PER_COLOUR_CHANNEL = 1;
				defparam VGA.BACKGROUND_IMAGE = "background.mif";
endmodule


