input:=325489;

list:=[[0,0,1]];

repeat
	x:=list[#list][1];
	y:=list[#list][2];
	list[#list+1]:=[x,y,0];
	if x ge y and x le -y then
		list[#list][1]+:=1;
	elif x gt y and x gt -y then
		list[#list][2]+:=1;
	elif y ge x and x gt -y then
		list[#list][1]-:=1;
	elif y gt x and x le -y then
		list[#list][2]-:=1;
	end if;
	for n in [1..#list-1] do
		if Abs(list[n][1]-list[#list][1]) le 1 and Abs(list[n][2]-list[#list][2]) le 1 then
			list[#list][3]+:=list[n][3];
		end if;
	end for;
until list[#list][3] gt input;

list[#list][3];