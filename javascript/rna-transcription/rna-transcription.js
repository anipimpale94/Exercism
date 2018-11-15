export const toRna = (dnaStrand) => {
 let dna = "";
 for (let letter of dnaStrand) {
  if (letter === 'G') dna = dna + 'C';
  else if (letter === 'C') dna = dna + 'G';
  else if (letter === 'T') dna = dna + 'A';
  else if (letter === 'A') dna = dna + 'U';
  else throw "Invalid input DNA.";
 }
 return dna;
}
