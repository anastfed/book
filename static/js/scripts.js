window.onload = function () {
    console.log("DOM loaded");

    $("div.content article.news div.rating span.thumb").on("click", "a", function (event) {
        if(event.target.className != "is-authenticated") {
            window.location = "/auth/login/";
        }
        var currHref = event.target.href;
        $.ajax({
            url: currHref + "ajax/",
            success: function (answer) {
                var newsPk = answer.news_pk;
                var rating = answer.rating;
                $("span#rating-" + newsPk).html(rating);
            },
        });
        event.preventDefault();
    });

    $(".books").on("click", "ul", function (event) {
        var bookId = event.target.id;
        var bookIdSplitted = bookId.split("-");
        var bookIdNum = bookIdSplitted.pop();

        $.ajax({
            url: "/categories/books/" + bookIdNum + "/ajax/",

            success: function (answer) {
                $(".book_description").html(answer.book_description);
                console.log("клик на книге вернулся от контроллера");
            },

        });
    });

    $(".book-categories").on("click", "ul li", function (event) {
        var bookCategoriesIdNum = event.target.id.split("-").pop();
        $.ajax({
            url: "/categories/book-categories/" + bookCategoriesIdNum + "/ajax/",

            success: function (answer) {
                $(".bookCategories_description").html(answer.bookCategories_description);
                console.log("клик на книге вернулся от контроллера");
            },

        });
    });

    function refreshActiveTall(currHref){
        $.ajax({
            url: currHref,
            success: function (answer) {
                $(".active-talk").html(answer.active_talk);
                $(".active-talk").css("display", "block");
                $(".send-message-form").html(answer.send_message);
                $(".send-message-form").css("display", "block");
            },
        });
    }
       $(".exchange-member").on("click", function (event) {
        var currHref = event.target.href;
        console.log(currHref, event.target)
        $.ajax({
            url: currHref,
            success: function (answer) {
                $(".exchange-members-list").css("height", "50px");
                $(".exchange-members-list").css("overflow", "auto");
                $(".active-talk").html(answer.active_talk);
                $(".active-talk").css("display", "block");
                $(".send-message-form").html(answer.send_message);
                $(".send-message-form").css("display", "block");
            },
        });
        event.preventDefault();
    });


    $(".exchange").on("submit", ".message-form", function (event) {
        event.preventDefault();
        var $messageForm = $(this);
        $.ajax({
            url: $messageForm.attr('action'),
            type: $messageForm.attr('method'),
            data: $messageForm.serialize(),
            success: function (answer) {
                console.log(answer);
            }
        });
    });
    }

    function editPlace(pk) {
        $.ajax({
            url: "/place/edit/" + pk + "/ajax/",
            success: function (answer) {
                $("#place-edit-form-" + answer.pk).html(answer.form);
                $("#place-edit-form-" + answer.pk).css("display", "block");
            },
        });

    function openForm() {
      document.getElementById("myForm").style.display = "block";
    }
    function closeForm() {
      document.getElementById("myForm").style.display = "none";
    }

    var chatTimer;
    var currHref
}

//        $(document).ready(function(){
//        //Обработка нажатия на кнопку "Вверх"
//        $("#up").click(function(){
//        //Необходимо прокрутить в начало страницы
//        var curPos=$(document).scrollTop();
//        var scrollTime=curPos/1.73;
//        $("body,html").animate({"scrollTop":0},scrollTime);
//        });
//
//        //Обработка нажатия на кнопку "Вниз"
//        $("#down").click(function(){
//        //Необходимо прокрутить в конец страницы
//        var curPos=$(document).scrollTop();
//        var height=$("body").height();
//        var scrollTime=(height-curPos)/1.73;
//        $("body,html").animate({"scrollTop":height},scrollTime);
//        });


        function createProduct(el) {
    let parrentCont = document.querySelector(".products");
    let card = document.createElement("div");
    card.classList.add("card");
    card.classList.add("product-" + counter);
    counter++;
    let cardContent = document.createElement("div");
    cardContent.classList.add("card-content");
    let cardImage = document.createElement("div");
    cardImage.classList.add("card-image");
    let isLikedCard = document.createElement("div");
    isLikedCard.classList.add("is-liked-card");
    let heartIcon = document.createElement("i");
    heartIcon.classList.add("fas");
    heartIcon.classList.add("fa-heart");
    isLikedCard.appendChild(heartIcon);
    let cardText = document.createElement("div");
    cardText.classList.add("card-text");
    let cardTitle = document.createElement("div");
    cardTitle.classList.add("card-title");
    let cardTitleSpan = document.createElement("span");
    cardTitleSpan.classList.add("text-bold");
    cardTitleSpan.innerHTML = el.name;
    cardTitle.appendChild(cardTitleSpan);
    let cardPrice = document.createElement("div");
    cardPrice.classList.add("card-price");
    let cardPriceSpan = document.createElement("span");
    cardPriceSpan.classList.add("text-bold");
    cardPriceSpan.innerHTML = "Цена: ";
    let cardSelfPrice = document.createElement("span");
    cardSelfPrice.classList.add("card-self-price");
    cardSelfPrice.innerHTML = "₽" + el.price;
    cardPrice.appendChild(cardPriceSpan);
    cardPrice.appendChild(cardSelfPrice);
    let cardDescription = document.createElement("div");
    cardDescription.classList.add("card-description");
    let cardDescriptionSpan = document.createElement("span");
    cardDescriptionSpan.classList.add("text-bold");
    cardDescriptionSpan.innerHTML = "Автор:";
    let cardDescriptionManualSpan = document.createElement("span");
    cardDescriptionManualSpan.classList.add("card-description-manual");
    cardDescriptionManualSpan.innerHTML = el.description;
    cardDescription.appendChild(cardDescriptionSpan);
    cardDescription.appendChild(cardDescriptionManualSpan);
    cardText.appendChild(cardTitle);
    cardText.appendChild(cardPrice);
    cardText.appendChild(cardDescription);
    cardImage.appendChild(isLikedCard);
    cardContent.appendChild(cardImage);
    cardContent.appendChild(cardText);
    card.appendChild(cardContent);
    let cardButtons = document.createElement("div");
    cardButtons.classList.add("card-buttons");
    let cardButtonMore = document.createElement("div");
    cardButtonMore.classList.add("card-button");
    cardButtonMore.classList.add("card-button-more");
    let cardButtonMoreSpan = document.createElement("span");
    cardButtonMoreSpan.classList.add("text-bold");
    cardButtonMoreSpan.classList.add("color-gray");
    cardButtonMoreSpan.innerHTML = "Описание";
    cardButtonMore.appendChild(cardButtonMoreSpan);
    let cardSaveButtons = document.createElement("div");
    cardSaveButtons.classList.add("card-save-buttons");
    let cardBuy = document.createElement("div");
    cardBuy.classList.add("card-button");
    cardBuy.classList.add("card-buy");
    let cardBuySpan = document.createElement("span");
    cardBuySpan.classList.add("text-bold");
    cardBuySpan.classList.add("color-white");
    cardBuySpan.innerHTML = "В избранное";
    cardBuy.appendChild(cardBuySpan);
    cardSaveButtons.appendChild(cardBuy);
    let cardAddInCart = document.createElement("div");
    cardAddInCart.classList.add("card-add-in-cart");
    let cartIcon = document.createElement("i");
    cartIcon.classList.add("fas");
    cartIcon.classList.add("fa-shopping-cart");
    cardAddInCart.appendChild(cartIcon);
    cardSaveButtons.appendChild(cardAddInCart);
    cardButtons.appendChild(cardButtonMore);
    cardButtons.appendChild(cardSaveButtons);
    card.appendChild(cardButtons);
    parrentCont.appendChild(card);
}

function generateProductInToCart(parent, idProd) {
    let cartProduct = document.createElement("div");
    cartProduct.classList.add("cart-product");
    cartProduct.classList.add("product-" + idProd);

    let cartProductInfo = document.createElement("div");
    cartProductInfo.classList.add("cart-product-info");

    let cartProductImg = document.createElement("div");
    cartProductImg.classList.add("cart-product-img");

    cartProductInfo.appendChild(cartProductImg);

    let cartProductText = document.createElement("div");
    cartProductText.classList.add("cart-product-text");

    let cartProductTitle = document.createElement("div");
    cartProductTitle.classList.add("cart-product-title");

    let cartProductTitleText = document.createElement("span");
    cartProductTitleText.classList.add("cart-product-title-text");
    cartProductTitleText.innerHTML = products[idProd - 1].name;

    cartProductTitle.appendChild(cartProductTitleText);
    cartProductText.appendChild(cartProductTitle);
    cartProductInfo.appendChild(cartProductText);

    let cartProductPrice = document.createElement("div");
    cartProductPrice.classList.add("cart-product-price");

    let cartProductPriceText = document.createElement("span");
    cartProductPriceText.classList.add("cart-product-price-text");
    cartProductPriceText.innerHTML = "Цена: ";

    let cartProductSelfPrice = document.createElement("span");
    cartProductSelfPrice.classList.add("self-price");
    cartProductSelfPrice.innerHTML = "₽" + products[idProd - 1].price;

    cartProductPrice.appendChild(cartProductPriceText);
    cartProductPriceText.appendChild(cartProductSelfPrice);
    cartProductText.appendChild(cartProductPrice);

    let cartProductButtons = document.createElement("div");
    cartProductButtons.classList.add("cart-product-buttons");

    let cartProductButtonMore = document.createElement("div");
    cartProductButtonMore.classList.add("cart-product-button-more");

//    let cartProductButtonMoreText = document.createElement("span");
//    cartProductButtonMoreText.innerHTML = "подробнее";
//    cartProductButtonMore.appendChild(cartProductButtonMoreText);

    cartProductButtons.appendChild(cartProductButtonMore);

    let cartProductButtonDel = document.createElement("div");
    cartProductButtonDel.classList.add("cart-product-button-del");

    let cartProductButtonDelText = document.createElement("span");
    cartProductButtonDelText.innerHTML = "удалить";
    cartProductButtonDel.appendChild(cartProductButtonDelText);

    cartProductButtons.appendChild(cartProductButtonDel);

    let cartProductButtonBye = document.createElement("div");
    cartProductButtonBye.classList.add("cart-product-button-buy");

//    let cartProductButtonByeText = document.createElement("span");
//    cartProductButtonByeText.innerHTML = "купить ₽";
//    cartProductButtonBye.appendChild(cartProductButtonByeText);


    cartProductButtons.appendChild(cartProductButtonBye);

    cartProduct.appendChild(cartProductInfo);
    cartProduct.appendChild(cartProductButtons);
    parent.appendChild(cartProduct);
}

window.onload = function () {
    let cartAmount = 0;
    cartScore = document.querySelector(".cart-score");
    cart = document.querySelector(".cart-products");
    cartScore.innerHTML = cartAmount;
    cartArray = [];
    products = [
        {
            id: 1,
            name: "Институт",
            price: 752,
            description: "Стивен Кинг",
            img: ""
        },
        {
            id: 2,
            name: "Не открывать! Кусается!(#1)",
            price: 325,
            description: "Шарлотта Хаберзак",
            img: ""
        },
        {
            id: 3,
            name: "Исскуство ясно мыслить",
            price: 954,
            description: "Рольф Доббелли",
            img: ""
        },
        {
            id: 4,
            name: "Заводной апельсин",
            price: 170,
            description: "Энтони Бёрджесс",
            img: ""
        },
        {
            id: 5,
            name: "Маленькая злая книга",
            price: 296,
            description: "Магнус Мист",
            img: ""
        },
        {
            id: 6,
            name: "Маленькая злая книга 2",
            price: 293,
            description: "Магнус Мист",
            img: ""
        },
         {
            id: 7,
            name: "Игры,в которые играют люди",
            price: 303,
            description: "Эрик Берн",
            img: ""
        },
         {
            id: 8,
            name: "Бедная Лиза",
            price: 120,
            description: "Николай Карамзин",
            img: ""
        },
         {
            id: 9,
            name: "Куриный бульон для души",
            price: 310,
            description: "Эми Ньюмарк",
            img: ""
        },
         {
            id: 10,
            name: "Время Библиомантов",
            price: 475,
            description: "Кай Майер",
            img: ""
        }
    ];
    counter = 1;
    products.forEach(function (el) {
        createProduct(el);
    });

    let addInCartButton = document.querySelectorAll(".card-add-in-cart");

    addInCartButton.forEach(function (element) {
        element.addEventListener("click", function () {
            let cardId = +(element.parentNode.parentNode.parentNode.classList[1].match(/\d+/)[0]);
            cartAmount++;
            cartScore.innerHTML = cartAmount;
            generateProductInToCart(cart, cardId);
            cartArray.push(cardId);

        });
    });

//    $(function(){
//      var loc = window.location.search;
//    if(loc == "?order=ok"){
//        $(".order").css("display", "block");
//    }
//    });

$('#signup').click(function() {
  $('.pinkbox').css('transform', 'translateX(80%)');
  $('.signin').addClass('nodisplay');
  $('.signup').removeClass('nodisplay');
});

$('#signin').click(function() {
  $('.pinkbox').css('transform', 'translateX(0%)');
  $('.signup').addClass('nodisplay');
  $('.signin').removeClass('nodisplay');
});


};