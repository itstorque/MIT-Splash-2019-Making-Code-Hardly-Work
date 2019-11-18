

for (var i = 0; i < find_length([for (i of [0,0,0,0,0]]) x]); i++) { // i < 5

  console.log(i)

}

function find_length(item) {

  n = [].length // = 0

  for (var i = 0; i < item.length; i++) {

    console.log([n])

    n += [n].length // += 1

  }

  return n //returns item.length

}
