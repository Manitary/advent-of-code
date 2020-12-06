F:=Open("input5.txt","r");

bp:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~bp,s);
end while;

function ComputeRow(pass)
	_, code:=Regexp("[BF]+",pass);
	code:=[x eq "B" select 1 else 0:x in Reverse(Eltseq(code))];
	return Seqint(code,2);
end function;

function ComputeCol(pass)
	_, code:=Regexp("[LR]+",pass);
	code:=[x eq "R" select 1 else 0:x in Reverse(Eltseq(code))];
	return Seqint(code,2);
end function;

function ComputeID(pass)
	return ComputeRow(pass)*8+ComputeCol(pass);
end function;

bpID:={ComputeID(pass): pass in bp};
PrintFile("day05,txt",Max(bpID));

candidates:={r*8+c:r in [1..126],c in [0..7]} diff bpID;
exists(seat){x:x in candidates|x+1 notin candidates and x-1 notin candidates};
PrintFile("day05.txt",seat);
