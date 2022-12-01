F:=Open("input14.txt","r");

reactions:=[**];
G:=EmptyDigraph(1);
AssignLabel(VertexSet(G).1,"FUEL");
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	obj:=[*SequenceToList(Split(l,", ")):l in Split(s,"=>")*];
	obj[2,1]:=StringToInteger(obj[2,1]);
	if obj[2,2] notin Labels(VertexSet(G)) then
		AddVertex(~G,obj[2,2]);
	end if;
	for i in [1..#obj[1]] do
		if i mod 2 eq 1 then
			obj[1,i]:=StringToInteger(obj[1,i]);
		else
			if obj[1,i] notin Labels(VertexSet(G)) then
				AddVertex(~G,obj[1,i]);
			end if;
			G+:=[VertexSet(G).Index(Labels(VertexSet(G)),obj[2,2]),VertexSet(G).Index(Labels(VertexSet(G)),obj[1,i])];
		end if;
	end for;
	Append(~reactions,obj);
end while;
V:=VertexSet(G);

function FindReagents(item,quant)
	exists(formula){x:x in reactions|x[2,2] eq item};
	return [*[*formula[1,i]*((quant div formula[2,1])+(quant mod formula[2,1] eq 0 select 0 else 1)),formula[1,i+1]*]:i in [1..#formula[1] by 2]*];
end function;

function FindReagentsExact(item,quant)
	exists(formula){x:x in reactions|x[2][2] eq item};
	return [*[*(formula[1,i])*(quant/formula[2,1]),formula[1,i+1]*]:i in [1..#formula[1] by 2]*];
end function;

materials:=[*[*1,"FUEL"*]*];
while true do
	ngbh:=[Exclude({V!x:x in VertexSet(Component(V.Index(Labels(V),m[2])))} meet {V.Index(Labels(V),x[2]):x in materials},V.Index(Labels(V),m[2])):m in materials];
	if exists(item){m:m in materials|m[2] ne "ORE" and m[2] notin &join{{Label(v):v in list}:list in ngbh}} then
	new_items:=FindReagents(item[2],item[1]);
	Remove(~materials,Index(materials,item));
	for thing in new_items do
		idx:=Index([x[2]:x in materials],thing[2]);
		if idx gt 0 then
			materials[idx,1]:=(materials[idx,1])+(thing[1]);
		else
			Append(~materials,thing);
		end if;
	end for;
	else
		break;
	end if;
end while;
ore:=materials[1,1];
PrintFile("day14.txt",ore);

materials:=[*[*1,"FUEL"*]*];
while true do
	ngbh:=[Exclude({V!x:x in VertexSet(Component(V.Index(Labels(V),m[2])))} meet {V.Index(Labels(V),x[2]):x in materials},V.Index(Labels(V),m[2])):m in materials];
	if exists(item){m:m in materials|m[2] ne "ORE" and m[2] notin &join{{Label(v):v in list}:list in ngbh}} then
	new_items:=FindReagentsExact(item[2],item[1]);
	Remove(~materials,Index(materials,item));
	for thing in new_items do
		idx:=Index([x[2]:x in materials],thing[2]);
		if idx gt 0 then
			materials[idx,1]:=(materials[idx,1])+(thing[1]);
		else
			Append(~materials,thing);
		end if;
	end for;
	else
		break;
	end if;
end while;
ore_ex:=materials[1,1];
cargo:=10^12;
PrintFile("day14.txt",Floor((cargo/ore_ex) - ((ore - ore_ex)/ore_ex)));
