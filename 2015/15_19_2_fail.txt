//this is not gonna work, probably

replacements:=[["Al","ThF"],["Al","ThRnFAr"],["B","BCa"],["B","TiB"],["B","TiRnFAr"],["Ca","CaCa"],["Ca","PB"],["Ca","PRnFAr"],["Ca","SiRnFYFAr"],["Ca","SiRnMgAr"],["Ca","SiTh"],["F","CaF"],["F","PMg"],["F","SiAl"],["H","CRnAlAr"],["H","CRnFYFYFAr"],["H","CRnFYMgAr"],["H","CRnMgYFAr"],["H","HCa"],["H","NRnFYFAr"],["H","NRnMgAr"],["H","NTh"],["H","OB"],["H","ORnFAr"],["Mg","BF"],["Mg","TiMg"],["N","CRnFAr"],["N","HSi"],["O","CRnFYFAr"],["O","CRnMgAr"],["O","HP"],["O","NRnFAr"],["O","OTi"],["P","CaP"],["P","PTi"],["P","SiRnFAr"],["Si","CaSi"],["Th","ThCa"],["Ti","BP"],["Ti","TiTi"],["e","HF"],["e","NAl"],["e","OMg"]];
molecule:="CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl";
molecule:=[molecule[i]:i in [1..#molecule]];
to_replace:={r[2]:r in replacements};
maxword:=Maximum([#word:word in to_replace]);
steps:=0;
procedure find_replace(~molecule,~steps)
	for i in [1..#molecule-maxword+1] do
		word:="";
		for j in [0..maxword-1] do
			word*:=molecule[i+j];
			if word in to_replace then
				steps+:=1;
				for k in [0..j] do
					Remove(~molecule,i);
				end for;
				for r in replacements do
					if r[2] eq word then
						Insert(~molecule,i,i-1,[r[1][c]:c in [1..#r[1]]]);
						break;
					end if;
				end for;
				break i;
			end if;
		end for;
	end for;
end procedure;

repeat
	find_replace(~molecule,~steps);
until molecule eq ["e"];
steps;				