F:=Open("input9.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input, [StringToInteger(c):c in Eltseq(s)]);
end while;

sum:=0;
for r in [1..#input], c in [1..#input[1]] do
	low:=true;
	for i, j in [-1..1] do
		if Abs(i)+Abs(j) eq 1 and r+i ge 1 and r+i le #input and c+j ge 1 and c+j le #input[1] then
				if input[r+i,c+j] le input[r,c] then
					low:=false;
					break i;
				end if;
			end if;
	end for;
	if low then
		sum+:=input[r,c]+1;
	end if;
end for;

PrintFile("day09.txt", sum);

GetNGBH:=function(input,basin,coords)
	for p in basin do
		for i, j in [-1..1] do
			if Abs(i)+Abs(j) eq 1 and <p[1]+i,p[2]+j> in coords and <p[1]+i,p[2]+j> notin basin then 
				if input[p[1]+i,p[2]+j] ne 9 then
					return true, <p[1]+i,p[2]+j>;
				end if;
			end if;
		end for;
	end for;
	return false, false;
end function;

sizes:=[];
coords:={<r,c>:r in [1..#input], c in [1..#input[1]]};
while #coords gt 0 do
	basin:={};
	pt:=Random(coords);
	Exclude(~coords,pt);
	if input[pt[1],pt[2]] ne 9 then
		Include(~basin,pt);
		repeat
			found, newpoint:=GetNGBH(input,basin,coords);
			if found then
				Exclude(~coords,newpoint);
				Include(~basin,newpoint);
			end if;
		until not found;
		Append(~sizes,#basin);
	end if;
end while;

Sort(~sizes);
sizesprod:=sizes[#sizes] * sizes[#sizes-1] * sizes[#sizes-2];

PrintFile("day09.txt", sizesprod);
