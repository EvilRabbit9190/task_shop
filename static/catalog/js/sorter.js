'use strict';

{
    // Открытие меню сортировки
    const menu_sort = document.querySelector("#sortListBox")
    const button_sort = document.querySelector(".sort__dropdown-trigger")

    button_sort.onclick = function (e) {
        console.log("Click")
        if (menu_sort.className === "custom-select sort__select") {
            menu_sort.className = "custom-select sort__select sort__dropdown-open"
        } else {
            menu_sort.className = "custom-select sort__select"
        }
    }

    // // Выбор сортировки

    // // По популярности
    // const popular_sort = document.querySelector("#sortListBox-most-popular")
    // console.log('popular_sort: ', popular_sort)
    // popular_sort.onclick = function (e) {
    //     console.log("Popular")
    //     menu_sort.className = "custom-select sort__select"
    // }

    // // От меньшей цены к большей
    // const lot_to_high = document.querySelector("#sortListBox-price-low-to-high")
    // console.log('lot_to_high: ', lot_to_high)
    // lot_to_high.onclick = function (e) {
    //     console.log("Low to High")
    //     menu_sort.className = "custom-select sort__select"
    // }


    // // От большей цены к меньшей
    // const high_to_low = document.querySelector("#sortListBox-price-high-to-low")
    // console.log('high_to_low: ', high_to_low)
    // high_to_low.onclick = function (e) {
    //     console.log("High to Low")
    //     menu_sort.className = "custom-select sort__select"
    // }
}