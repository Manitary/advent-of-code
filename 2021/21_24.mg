F:=Open("input24.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input, Split(s, " "));
end while;

var:=AssociativeArray();
var["w"]:=0;
var["x"]:=0;
var["y"]:=0;
var["z"]:=0;

procedure Execute(~val, instr, mn, ~idx, ~crash)
	case instr[1]:
	when "inp":
		val[instr[2]]:=mn[idx];
		idx+:=1;
	when "add":
		val[instr[2]]+:=instr[3] in Keys(val) select val[instr[3]] else StringToInteger(instr[3]);
	when "mul":
		val[instr[2]]*:=instr[3] in Keys(val) select val[instr[3]] else StringToInteger(instr[3]);
	when "div":
		den:=instr[3] in Keys(val) select val[instr[3]] else StringToInteger(instr[3]);
		if den ne 0 then
			val[instr[2]]div:=instr[3] in Keys(val) select val[instr[3]] else StringToInteger(instr[3]);
		else
			crash:=true;
		end if;
	when "mod":
		num:=val[instr[2]];
		den:=instr[3] in Keys(val) select val[instr[3]] else StringToInteger(instr[3]);
		if num lt 0 or den le 0 then
			crash:=true;
		else
			val[instr[2]]mod:=den;
		end if;
	when "eql":
		val[instr[2]]:=val[instr[2]] eq (instr[3] in Keys(val) select val[instr[3]] else StringToInteger(instr[3])) select 1 else 0;
	end case;
end procedure;

for model in [41171183141291] do
	m:=Reverse(Intseq(model));
	if 0 in m then
		continue;
	end if;
	var["w"]:=0;
	var["x"]:=0;
	var["y"]:=0;
	var["z"]:=0;
	crash:=false;
	i:=1;
	for inst in input do
		Execute(~var, inst, m, ~i, ~crash);
		if crash then break; end if;
	end for;
	if not crash then
		if var["z"] eq 0 then
			model;
			break model;
		end if;
	end if;
end for;
