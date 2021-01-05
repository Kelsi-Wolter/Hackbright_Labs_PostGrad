"use strict";


// 1. isHometown

function isHometown(town) {
    town = town.toLowerCase();
    return town === 'san francisco'

}


// 2. getFullName
function getFullName(first, last) {
    return `${first.charAt(0).toUpperCase()}${first.slice(1)} ${last.charAt(0).toUpperCase()}${last.slice(1)}`
}


// 3. calculateTotal

function calculateTotal(basePrice, state, tax=0.05) {
    const subtotal = basePrice * (1 + tax);
    let fee = 0;
    if (state === 'CA') {
        fee = 0.03 * subtotal;        
    }
    else if (state === 'PA') {
        fee = 2
    }
    else if (state === 'MA') {
        if (basePrice <= 100) {
            fee = 1
        }
        else {
            fee = 3
        }
    }
    console.log(subtotal + fee)
}
