replacements:=[["Al","ThF"],["Al","ThRnFAr"],["B","BCa"],["B","TiB"],["B","TiRnFAr"],["Ca","CaCa"],["Ca","PB"],["Ca","PRnFAr"],["Ca","SiRnFYFAr"],["Ca","SiRnMgAr"],["Ca","SiTh"],["F","CaF"],["F","PMg"],["F","SiAl"],["H","CRnAlAr"],["H","CRnFYFYFAr"],["H","CRnFYMgAr"],["H","CRnMgYFAr"],["H","HCa"],["H","NRnFYFAr"],["H","NRnMgAr"],["H","NTh"],["H","OB"],["H","ORnFAr"],["Mg","BF"],["Mg","TiMg"],["N","CRnFAr"],["N","HSi"],["O","CRnFYFAr"],["O","CRnMgAr"],["O","HP"],["O","NRnFAr"],["O","OTi"],["P","CaP"],["P","PTi"],["P","SiRnFAr"],["Si","CaSi"],["Th","ThCa"],["Ti","BP"],["Ti","TiTi"],["e","HF"],["e","NAl"],["e","OMg"]];
molecule:="CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl";
molecule:=[molecule[i]:i in [1..#molecule]];
to_replace:={r[1]:r in replacements};
new_mol:={};
for i in [1..#molecule] do
	if molecule[i] in to_replace then
		for replacement in replacements do
			if replacement[1] eq molecule[i] then
				Include(~new_mol,Insert(Remove(molecule,i),i,i-1,[replacement[2][c]: c in [1..#replacement[2]]]));
			end if;
		end for;
	elif i lt #molecule and molecule[i]*molecule[i+1] in to_replace then
		for replacement in replacements do
			if replacement[1] eq molecule[i]*molecule[i+1] then
				Include(~new_mol,Insert(Remove(Remove(molecule,i),i),i,i-1,[replacement[2][c]: c in [1..#replacement[2]]]));
			end if;
		end for;
	end if;
end for;
#new_mol;