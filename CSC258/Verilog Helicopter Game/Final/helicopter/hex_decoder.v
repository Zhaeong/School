module hex_decoder(bcd_in, ss_out);
   input [3:0] bcd_in;
   output [0:6] ss_out;
   reg [0:6] ss_out;
   
   always @(bcd_in)
      case (bcd_in)
         4'b0000 :
            ss_out = 7'b0000001;
         4'b0001 :
            ss_out = 7'b1001111;
         4'b0010 :
            ss_out = 7'b0010010;
         4'b0011 :
            ss_out = 7'b0000110;
         4'b0100 :
            ss_out = 7'b1001100;
         4'b0101 :
            ss_out = 7'b0100100;
         4'b0110 :
            ss_out = 7'b1100000;
         4'b0111 :
            ss_out = 7'b0001111;
         4'b1000 :
            ss_out = 7'b0000000;
         4'b1001 :
            ss_out = 7'b0001100;
			default :
            ss_out = 7'b0000001;
      
      endcase
endmodule






