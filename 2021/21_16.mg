F:=Open("input16.txt","r");

input:=Gets(F);

hexdigits:=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"];
hexcodes:=Sort([[a,b,c,d]:a,b,c,d in [0,1]]);
Convert:=func<x|hexcodes[Index(hexdigits,x)]>;
SequenceToBinary:=func<x|SequenceToInteger(Reverse(x),2)>;

input:=&cat[Convert(input[i]):i in [1..#input]];

function ParseValue(list, i)
	if 0 notin [list[x]:x in [i..#list]] then
		return 0;
	end if;
	versionsum:=SequenceToBinary([list[j]:j in [i..i+2]]);
	type:=SequenceToBinary([list[j]:j in [i+3..i+5]]);
	j:=i+6;
	if type eq 4 then
		val:=[];
		repeat
			lead:=list[j];
			for k in [1..4] do
				j+:=1;
				Append(~val, list[j]);
			end for;
			j+:=1;
		until lead eq 0;
		total:=SequenceToBinary(val);
		return versionsum, j, total;
	else
		values:=[];
		if list[j] eq 0 then
			len:=SequenceToBinary([list[k]:k in [j+1..j+15]]);
			j+:=16;
			k:=j;
			j+:=len;
			repeat
				ver,k,val:=ParseValue(list,k);
				versionsum+:=ver;
				Append(~values,val);
			until k eq j;
		else
			num:=SequenceToBinary([list[k]:k in [j+1..j+11]]);
			j+:=12;
			for k in [1..num] do
				ver,j,val:=ParseValue(list,j);
				versionsum+:=ver;
				Append(~values,val);
			end for;
		end if;
		case type:
		when 0:
			total:=&+values;
		when 1:
			total:=&*values;
		when 2:
			total:=Min(values);
		when 3:
			total:=Max(values);
		when 5:
			total:=values[1] gt values[2] select 1 else 0;
		when 6:
			total:=values[1] lt values[2] select 1 else 0;
		when 7:
			total:=values[1] eq values[2] select 1 else 0;
		end case;
		return versionsum, j, total;
	end if;
end function;

val, _, total:=ParseValue(input,1);

PrintFile("day16.txt",val);
PrintFile("day16.txt",total);

