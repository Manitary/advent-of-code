F:=Open("input20.txt","r");

algorithm:=Gets(F);
Gets(F);
input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,Eltseq(s));
end while;

function EnhancePixel(y,x,picture,filler)
	pic:=[];
	for j in [-1..1] do
		for i in [-1..1] do
			if y+j ge 1 and y+j le #picture and x+i ge 1 and x+i le #picture[1] then
				Append(~pic, picture[y+j,x+i] eq "#" select 1 else 0);
			else
				Append(~pic,filler eq "#" select 1 else 0);
			end if;
		end for;
	end for;
	return algorithm[SequenceToInteger(Reverse(pic),2)+1];
end function;

procedure EnhancePicture(~picture, filler)
	newpic:=[];
	Insert(~picture, 1, [filler:i in [1..#picture[1]]]);
	Append(~picture, [filler:i in [1..#picture[1]]]);
	for i in [1..#picture] do
		Insert(~picture[i], 1, filler);
		Append(~picture[i], filler);
	end for;
	for y in [1..#picture] do
		Append(~newpic,[]);
		for x in [1..#picture[1]] do
			newpic[y,x]:=EnhancePixel(y,x,picture,filler);
		end for;
	end for;
	picture:=newpic;
end procedure;

filler:=".";
for i in [1..50] do
	EnhancePicture(~input,filler);
	filler:=filler eq "." select algorithm[1] else algorithm[#algorithm];
	if i in [2,50] then
		lit:=0;
		for y in [1..#input] do
			for x in [1..#input[1]] do
				if input[y,x] eq "#" then
					lit+:=1;
				end if;
			end for;
		end for;
		PrintFile("day20.txt", lit);
	end if;
end for;
