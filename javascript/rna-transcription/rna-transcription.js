export const toRna = (dnaStrand) => {
 let dna = "";
 for (let letter of dnaStrand) {
  if (letter === 'G') dna = dna + 'C';
  if (letter === 'C') dna = dna + 'G';
  if (letter === 'T') dna = dna + 'A';
  if (letter === 'A') dna = dna + 'U';
 }
 return dna;
}
