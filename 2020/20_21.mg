F:=Open("input21.txt","r");

food:=[];
food_allergen:=[];
ingr_food:=AssociativeArray();
aller_food:=AssociativeArray();
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	a:=Split(s,"(");
	Append(~food,Split(a[1]," "));
	if #a gt 1 then
		Append(~food_allergen,Remove(Split(a[2],", )"),1));
	else
		Append(~food_allergen,[]);
	end if;
	for i in food[#food] do
		if i in Keys(ingr_food) then
			ingr_food[i] cat:= [#food];
		else
			ingr_food[i]:=[#food];
		end if;
	end for;
	for i in food_allergen[#food_allergen] do
		if i in Keys(aller_food) then
			aller_food[i] cat:= [#food_allergen];
		else
			aller_food[i]:=[#food_allergen];
		end if;
	end for;
end while;
ingredients:=Keys(ingr_food);
allergens:=SetToSequence(Keys(aller_food));

candidates:=[SetToSequence(&meet{SequenceToSet(food[x]):x in aller_food[a]}):a in allergens];
while exists(i){x[1]:x in candidates|#x eq 1 and exists(j){y:y in candidates|x[1] in y and y ne x}} do
	Exclude(~candidates[Index(candidates,j)],i);
end while;
candidates:=[c[1]:c in candidates];

safecount:=0;
for i in ingredients do
	if i notin candidates then
		safecount+:=#ingr_food[i];
	end if;
end for;
PrintFile("day21.txt",safecount);

ParallelSort(~allergens,~candidates);
dangerlist:="";
for i in [1..#candidates] do
	dangerlist*:=candidates[i];
	if i ne #candidates then
		dangerlist*:=",";
	end if;
end for;
PrintFile("day21.txt",dangerlist);
