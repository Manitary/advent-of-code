F:=Open("input24.txt","r");

unit:=recformat<Faction:MonStgElt,Number:Integers(),HitPoints:Integers(),Attack:Integers(),AttackType:MonStgElt,Initiative:Integers(),Immunities:SetEnum,Weaknesses:SetEnum>;

procedure fill_army(~armies:faction:="None")
	while true do
		s:=Gets(F);
		if IsEof(s) or #s lt 2 then
			break;
		end if;
		_,_,n:=Regexp("([0-9]+) units",s);
		_,_,hp:=Regexp("([0-9]+) hit points",s);
		_,_,atk:=Regexp("([0-9]+) ([a-z]+) damage",s);
		_,_,i:=Regexp("initiative ([0-9]+)",s);
		b1,_,imm:=Regexp("immune to ([a-z, ]+)(;|\\))",s);
		b2,_,wk:=Regexp("weak to ([a-z, ]+)(;|\\))",s);
		Append(~armies,rec<unit|
			Faction:=faction,
			Number:=StringToInteger(n[1]),
			HitPoints:=StringToInteger(hp[1]),
			Attack:=StringToInteger(atk[1]),
			AttackType:=atk[2],
			Initiative:=StringToInteger(i[1]),
			Immunities:=b1 select SequenceToSet(Split(imm[1],", ")) else {},
			Weaknesses:=b2 select SequenceToSet(Split(wk[1],", ")) else {}
			>);
	end while;
end procedure;

armies:=[];
while true do
	t:=Gets(F);
	if IsEof(t) then
		break;
	end if;
	if Regexp("Immune",t) then
		fill_army(~armies:faction:="ImmuneSystem");
	elif Regexp("Infection",t) then
		fill_army(~armies:faction:="Infection");
	end if;
end while;

eff_power:=func<u|u`Number * u`Attack>;
priority:=func<u1,u2|eff_power(u1) eq eff_power(u2) select u2`Initiative-u1`Initiative else eff_power(u2)-eff_power(u1)>;
turn_order:=func<u1,u2|u2`Initiative-u1`Initiative>;
damage:=func<u1,u2|eff_power(u1)*(u1`Faction eq u2`Faction select 0 else 1)*(u1`AttackType in u2`Immunities select 0 else 1)*(u1`AttackType in u2`Weaknesses select 2 else 1)>;

function target_selection(armies)
	targets:=[];
	available:=[i:i in [1..#armies]];
	for a in [1..#armies] do
		dmg:=[<damage(armies[a],armies[d]),eff_power(armies[d]),armies[d]`Initiative>:d in available];
		ParallelSort(~dmg,~available);
		if dmg[#dmg,1] ne 0 then
			targets[a]:=available[#available];
			Prune(~available);
		else
			targets[a]:=0;
		end if;
		Sort(~available);
	end for;
	return targets;
end function;

procedure play_turn(~armies)
	Sort(~armies,priority);
	targets:=target_selection(armies);
	armies,perm:=Sort(armies,turn_order);
	targets:=[targets[i^perm] eq 0 select 0 else targets[i^perm]^perm^-1:i in [1..#targets]];
	for a in [1..#armies] do
		if armies[a]`Number gt 0 and targets[a] ne 0 then
			armies[targets[a]]`Number-:=damage(armies[a],armies[targets[a]]) div armies[targets[a]]`HitPoints;
		end if;
	end for;
	armies:=[armies[i]:i in [1..#armies]|armies[i]`Number gt 0];
end procedure;

base_armies:=armies;
repeat
	play_turn(~armies);
until #{u`Faction:u in armies} eq 1;

survivors:=func<a|&+{*u`Number:u in a*}>;

boost:=-1;
repeat
	boost+:=1;
	armies:=base_armies;
	for i in [1..#armies] do
		armies[i]`Attack+:=armies[i]`Faction eq "ImmuneSystem" select boost else 0;
	end for;
	repeat
		hp:={*u`Number:u in armies*};
		play_turn(~armies);
		if {*u`Number:u in armies*} eq hp then
			break;
		end if;
	until #{u`Faction:u in armies} eq 1;
	if boost eq 0 then
		PrintFile("day24.txt",survivors(armies));
	end if;
until {u`Faction:u in armies} eq {"ImmuneSystem"};
PrintFile("day24.txt",survivors(armies));
