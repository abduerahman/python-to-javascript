function ran(x){
    for (let i =0; i < 100; i += 1 ) {
          if (i % 2 == 0 ) {
            console.log('even')
        }
        else{
            console.log('odd')
        }
    }
    return 0
}
console.log(ran(100))