F:=Open("input8.txt","r");
input:=Gets(F);
width:=25;
height:=6;

layers:=[[[input[(l-1)*width*height+(h-1)*width+w]:w in [1..width]]:h in [1..height]]:l in [1..#input div (w*h)]];

_,min0:=Min([Multiplicity(&cat(l),"0"):l in layers]);
PrintFile("day08.txt",Multiplicity(&cat(layers[min0]),"1")*Multiplicity(&cat(layers[min0]),"2"));

for h in [1..height] do
	line:="";
	for w in [1..width] do
		for l in [1..#layers] do
			if layers[l,h,w] ne "2" then
				line*:=layers[l,h,w];
				break;
			end if;
		end for;
	end for;
	PrintFile("day08.txt",line);
end for;	
