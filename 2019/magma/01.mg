ModuleFuel:=func<mass|(mass div 3)-2>;

F:=Open("input1.txt","r");
fuel_tot:=0;
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	fuel_tot+:=ModuleFuel(StringToInteger(s));
end while;
PrintFile("day01.txt",fuel_tot);

function ModuleFuelCorrect(mass,tot)
	fuel:=ModuleFuel(mass);
	if fuel le 0 then
		return tot;
	else		
		return ModuleFuelCorrect(fuel,tot+fuel);
	end if;
end function;

F:=Open("input1.txt","r");
fuel_tot_real:=0;
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	fuel_tot_real+:=ModuleFuelCorrect(StringToInteger(s),0);
end while;
PrintFile("day01.txt",fuel_tot_real);
