boss:=[71,10];
you:=[50,500];
timer:=[0,0,0];
mana_spent:=0;
min_mana:=0;

RF:=recformat<name:MonStgElt,cost:Integers(),damage:Integers(),dot:Integers(),armor:Integers(),heal:Integers(),mana:Integers(),timer:Integers(),active:Integers()>;
m:=rec<RF|name:="M",cost:=53,damage:=4>;
d:=rec<RF|name:="D",cost:=73,damage:=2,heal:=2>;
s:=rec<RF|name:="S",cost:=113,armor:=7,timer:=6,active:=0>;
p:=rec<RF|name:="P",cost:=173,dot:=3,timer:=6,active:=0>;
r:=rec<RF|name:="R",cost:=229,mana:=101,timer:=5,active:=0>;
spells:=[m,d,s,p,r];

procedure active_spell(~spells,~boss,~you)
	if spells[3]`active gt 0 then
		spells[3]`active-:=1;
	end if;
	if spells[4]`active gt 0 then
		boss[1]-:=spells[4]`dot;
		spells[4]`active-:=1;
	end if;
	if spells[5]`active gt 0 then
		you[2]+:=spells[5]`mana;
		spells[5]`active-:=1;
	end if;
end procedure;

procedure execute_spell(spell_name,~you,~boss,~spells)
	for i in [1..#spells] do
		if spells[i]`name eq spell_name then
			for prop in Names(RF) do
				if assigned spells[i]``prop then
					case prop:
						when "cost":
							you[2]-:=spells[i]``prop;
						when "damage":
							boss[1]-:=spells[i]``prop;
						when "dot":
							spells[i]`active:=spells[i]`timer;
						when "armor":
							spells[i]`active:=spells[i]`timer;
						when "heal":
							you[1]+:=spells[i]``prop;
						when "mana":
							you[2]+:=spells[i]``prop;
					end case;
				end if;
			end for;
		end if;
	end for;
end procedure;
	
forward your_turn,play;
function boss_turn()
	you-:=spells[3]`active gt 0 select Maximum(1,boss[2]-spells[3]`armor) else boss[2];
	active_spell(~spells,~boss,~you);
	play;
end function;

function your_turn(spell)
	execute_spell();
	active_spell(~spells,~boss,~you);
	boss_turn();
end function;

boss:=[71,10];
you:=[50,500];
min_mana:=0;
mana_spent:=0;
	
procedure play(boss,you,~min_mana,~mana_spent)
	repeat
		oom:=true;
		for spell in spells do
			if spell`cost lt you[2] and (assigned spell`active select (spell`active eq 0) else true) then
				oom:=false;
				mana_spent+:=spell`cost;
				your_turn(spell`name);
			end if;
		end for;
	until oom;
	min_mana gt 0 select Minimum(min_mana,mana_spent
end procedure;

play(boss,you,~min_mana,~mana_spent);
min_mana;