from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r'''
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">

<title>ALL IN ME : ชอบอยู่บ้าน</title>

<style>

/* =========================================================
   RESET
========================================================= */

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html,
body {
    width: 100%;
    height: 100%;
    overflow: hidden;

    background: #fffbf7;

    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        "Noto Sans Thai",
        Arial,
        sans-serif;

    color: #29231f;
}

button {
    font-family: inherit;
}


/* =========================================================
   APP
========================================================= */

#app {
    position: fixed;
    inset: 0;

    width: 100%;
    height: 100%;

    overflow: hidden;

    background: #fffbf7;
}


/* =========================================================
   PAGE SYSTEM
========================================================= */

.page {
    position: absolute;
    inset: 0;

    width: 100%;
    height: 100%;

    overflow: hidden;

    transition:
        transform 1.35s cubic-bezier(.77, 0, .18, 1);
}


/* PAGE 1 */

#page1 {
    z-index: 20;

    background: #fffbf7;

    transform: translateY(0);
}


/* PAGE 2 */

#page2 {
    z-index: 10;

    background: #fffbf7;

    transform: translateY(100%);
}


body.entered #page1 {
    transform: translateY(-100%);
}

body.entered #page2 {
    transform: translateY(0);
}


/* =========================================================
   PAGE 1 — WELCOME
========================================================= */

.welcome-art {
    position: absolute;
    inset: 0;

    overflow: hidden;

    background:
        radial-gradient(
            circle at 82% 35%,
            #f1e2d7 0%,
            #fffbf7 45%,
            #fffbf7 100%
        );
}


/* =========================================================
   AI / ILLUSTRATION STYLE
========================================================= */

.ai-man {
    position: absolute;

    width: 280px;
    height: 500px;

    right: 8%;
    top: 9%;

    border-radius:
        48% 48%
        18% 18%;

    background:

        radial-gradient(
            circle at 50% 15%,
            #3e322c 0 11%,
            transparent 11.5%
        ),

        radial-gradient(
            ellipse at 50% 25%,
            #d6a47d 0 13%,
            transparent 13.5%
        ),

        linear-gradient(
            160deg,
            #70594b 0 48%,
            #403631 49% 100%
        );

    opacity: .78;

    filter:
        drop-shadow(
            0 25px 30px
            rgba(55,40,30,.12)
        );
}


/* CHIHUAHUA 1 */

.ai-dog-one {
    position: absolute;

    width: 280px;
    height: 310px;

    right: 29%;
    bottom: -30px;

    border-radius:
        48% 48%
        42% 42%;

    background:

        radial-gradient(
            circle at 35% 28%,
            #241d1a 0 7px,
            transparent 8px
        ),

        radial-gradient(
            circle at 67% 28%,
            #241d1a 0 7px,
            transparent 8px
        ),

        radial-gradient(
            ellipse at 50% 58%,
            #d89b62 0 42%,
            #a96e43 43% 100%
        );

    transform: rotate(-7deg);

    filter:
        drop-shadow(
            0 25px 30px
            rgba(55,40,30,.12)
        );
}

.ai-dog-one::before,
.ai-dog-one::after {
    content: "";

    position: absolute;

    top: -48px;

    width: 100px;
    height: 120px;

    background: #9d623c;

    border-radius:
        20% 75%
        20% 75%;
}

.ai-dog-one::before {
    left: 5px;
    transform: rotate(-25deg);
}

.ai-dog-one::after {
    right: 5px;
    transform: rotate(25deg);
}


/* CHIHUAHUA 2 */

.ai-dog-two {
    position: absolute;

    width: 235px;
    height: 270px;

    right: -15px;
    bottom: -15px;

    border-radius:
        48% 48%
        42% 42%;

    background:

        radial-gradient(
            circle at 35% 30%,
            #30251f 0 7px,
            transparent 8px
        ),

        radial-gradient(
            circle at 67% 30%,
            #30251f 0 7px,
            transparent 8px
        ),

        radial-gradient(
            ellipse at 50% 58%,
            #e0bd94 0 42%,
            #b2865d 43% 100%
        );

    transform: rotate(6deg);

    filter:
        drop-shadow(
            0 25px 30px
            rgba(55,40,30,.12)
        );
}

.ai-dog-two::before,
.ai-dog-two::after {
    content: "";

    position: absolute;

    top: -40px;

    width: 82px;
    height: 105px;

    background: #a9794f;

    border-radius:
        20% 75%
        20% 75%;
}

.ai-dog-two::before {
    left: 4px;
    transform: rotate(-25deg);
}

.ai-dog-two::after {
    right: 4px;
    transform: rotate(25deg);
}


/* =========================================================
   WELCOME OVERLAY
========================================================= */

.welcome-overlay {
    position: absolute;
    inset: 0;

    z-index: 5;

    background:
        linear-gradient(
            90deg,
            rgba(255,251,247,.99) 0%,
            rgba(255,251,247,.94) 35%,
            rgba(255,251,247,.58) 63%,
            rgba(255,251,247,.08) 100%
        );
}


/* =========================================================
   WELCOME CONTENT
========================================================= */

.welcome-content {
    position: relative;

    z-index: 10;

    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: center;

    padding:
        40px
        clamp(24px, 7vw, 110px);
}


.brand {
    position: absolute;

    top: clamp(25px, 5vh, 55px);
    left: clamp(24px, 7vw, 110px);
}


.brand-name {
    font-size:
        clamp(30px, 4vw, 58px);

    font-weight: 950;

    letter-spacing: -3px;
}


.brand-tagline {
    margin-top: 3px;

    font-size:
        clamp(15px, 1.5vw, 21px);

    font-weight: 700;
}


.promo {
    display: inline-flex;

    width: fit-content;

    padding:
        12px 22px;

    margin-bottom: 22px;

    border-radius: 999px;

    background: #24201d;

    color: #ffffff;

    font-size:
        clamp(14px, 1.4vw, 20px);

    font-weight: 950;

    letter-spacing: 1px;

    box-shadow:
        0 12px 30px
        rgba(35,30,25,.16);
}


.hero {
    max-width: 700px;

    font-size:
        clamp(50px, 7vw, 105px);

    line-height: .91;

    letter-spacing: -5px;

    font-weight: 950;
}


.hero-accent {
    display: block;

    margin-top: 8px;

    color: #d45b38;
}


.description {
    max-width: 680px;

    margin-top: 28px;

    font-size:
        clamp(15px, 1.45vw, 21px);

    line-height: 1.65;

    font-weight: 600;

    color: #554943;
}


.bottom-note {
    position: absolute;

    bottom: 28px;
    left: clamp(24px, 7vw, 110px);

    color: #8a7e75;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: .7px;
}


/* =========================================================
   PAGE 2
========================================================= */

.category-page {
    position: relative;

    width: 100%;
    height: 100%;

    padding:
        clamp(20px, 4vw, 55px);
}


.category-background {
    position: absolute;
    inset: 0;

    background:

        radial-gradient(
            circle at 10% 10%,
            rgba(220,180,150,.20),
            transparent 30%
        ),

        radial-gradient(
            circle at 90% 85%,
            rgba(190,205,185,.20),
            transparent 32%
        ),

        #fffbf7;

    transition:
        filter .4s ease;
}


.category-content {
    position: relative;

    z-index: 5;

    width: min(1200px, 100%);
    height: 100%;

    margin: auto;

    display: flex;
    flex-direction: column;
}


.page-title {
    font-size:
        clamp(32px, 4vw, 58px);

    line-height: .95;

    font-weight: 950;

    letter-spacing: -3px;
}


.page-subtitle {
    margin-top: 8px;

    font-size: 14px;

    font-weight: 600;

    color: #82766e;
}


/* =========================================================
   เก็บโค้ด
   ข้อ 15
========================================================= */

.voucher-button {

    position: absolute;

    top: 0;
    right: 0;

    display: inline-flex;

    align-items: center;
    justify-content: center;

    gap: 9px;

    border: 0;

    cursor: pointer;

    padding:
        13px 21px;

    border-radius: 999px;

    background: #d9ffdf;

    color: #ff78dc;

    font-size: 14px;

    font-weight: 950;

    box-shadow:
        0 7px 18px
        rgba(90,80,70,.13);

    transition:
        transform .25s ease,
        box-shadow .25s ease;
}


.voucher-button:hover {

    transform:
        translateY(-3px)
        scale(1.03);

    box-shadow:
        0 12px 25px
        rgba(90,80,70,.18);
}


.voucher-button:active {

    transform:
        scale(.96);
}


/* TRUCK ICON */

.truck-icon {

    width: 20px;
    height: 20px;

    display: inline-flex;

    align-items: center;
    justify-content: center;

    flex-shrink: 0;
}


.truck-icon svg {

    width: 20px;
    height: 20px;

    fill: none;

    stroke: #ff78dc;

    stroke-width: 2;

    stroke-linecap: round;
    stroke-linejoin: round;
}


/* =========================================================
   CATEGORY GRID
========================================================= */

.category-grid {

    flex: 1;

    display: grid;

    grid-template-columns:
        repeat(5, minmax(0, 1fr));

    gap: 18px;

    align-items: center;

    padding-top: 25px;
}


.category-card {

    position: relative;

    height:
        min(47vh, 390px);

    border:
        1px solid
        rgba(70,55,45,.08);

    border-radius: 30px;

    background:
        rgba(255,255,255,.74);

    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);

    box-shadow:

        0 10px 30px
        rgba(50,40,30,.08),

        inset 0 1px 0
        rgba(255,255,255,.85);

    cursor: pointer;

    overflow: hidden;

    transition:

        transform .45s
        cubic-bezier(.2,.8,.2,1),

        filter .45s ease,

        opacity .45s ease,

        box-shadow .45s ease;

    z-index: 1;
}


.category-card:hover {

    transform:
        scale(1.075)
        translateY(-7px);

    box-shadow:
        0 25px 50px
        rgba(45,35,28,.18);

    z-index: 30;
}


.category-grid:hover
.category-card:not(:hover) {

    filter: blur(5px);

    opacity: .45;

    transform:
        scale(.97);
}


.category-inner {

    position: relative;

    width: 100%;
    height: 100%;

    padding: 25px;

    display: flex;

    flex-direction: column;

    justify-content: space-between;

    align-items: center;

    text-align: center;
}


/* =========================================================
   3D CATEGORY ART
========================================================= */

.icon-3d {

    width:
        clamp(105px, 9vw, 165px);

    height:
        clamp(105px, 9vw, 165px);

    margin-top: 15px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 34px;

    background:

        linear-gradient(
            145deg,
            #ffffff,
            #e9ded4
        );

    box-shadow:

        12px 16px 28px
        rgba(60,45,35,.14),

        -8px -8px 20px
        rgba(255,255,255,.90),

        inset 0 2px 5px
        rgba(255,255,255,.95);

    font-size:
        clamp(58px, 5.3vw, 94px);

    transform:
        perspective(700px)
        rotateX(5deg)
        rotateY(-6deg);

    transition:
        transform .4s ease;
}


.category-card:hover
.icon-3d {

    transform:
        perspective(700px)
        rotateX(0)
        rotateY(0)
        scale(1.07)
        translateY(-4px);
}


.category-name {

    width: 100%;

    font-size:
        clamp(14px, 1.35vw, 20px);

    line-height: 1.3;

    font-weight: 900;

    color: #2b2521;
}


.category-number {

    color: #a39890;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1px;
}


/* =========================================================
   POPUP
========================================================= */

.popup-layer {

    position: fixed;

    inset: 0;

    z-index: 100;

    display: flex;

    align-items: center;
    justify-content: center;

    padding: 20px;

    background:
        rgba(35,29,25,.34);

    backdrop-filter: blur(13px);
    -webkit-backdrop-filter: blur(13px);

    opacity: 0;

    visibility: hidden;

    pointer-events: none;

    transition:
        opacity .35s ease,
        visibility .35s ease;
}


.popup-layer.show {

    opacity: 1;

    visibility: visible;

    pointer-events: auto;
}


.popup {

    position: relative;

    width:
        min(760px, 100%);

    max-height:
        min(82vh, 720px);

    overflow-y: auto;

    padding:
        clamp(24px, 4vw, 42px);

    border-radius: 34px;

    background:
        rgba(255,251,247,.90);

    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);

    border:
        1px solid
        rgba(255,255,255,.78);

    box-shadow:

        0 35px 100px
        rgba(30,25,20,.27),

        inset 0 1px 0
        rgba(255,255,255,.95);

    transform:
        scale(.80)
        rotate(-2deg);

    opacity: 0;

    transition:
        transform .5s
        cubic-bezier(.2,.9,.2,1),

        opacity .35s ease;
}


.popup-layer.show .popup {

    transform:
        scale(1)
        rotate(0);

    opacity: 1;
}


.popup-title {

    font-size:
        clamp(28px, 4vw, 47px);

    font-weight: 950;

    letter-spacing: -2px;
}


.popup-subtitle {

    margin-top: 7px;

    font-size: 13px;

    font-weight: 600;

    color: #82766e;
}


/* =========================================================
   BRAND LIST
========================================================= */

.brand-list {

    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 12px;

    margin-top: 28px;
}


.brand-button {

    min-height: 62px;

    border:
        1px solid
        rgba(70,55,45,.08);

    border-radius: 18px;

    background:
        rgba(255,255,255,.78);

    color: #29231f;

    cursor: pointer;

    padding:
        14px 17px;

    text-align: left;

    font-size: 14px;

    font-weight: 850;

    box-shadow:
        0 7px 20px
        rgba(50,40,30,.06);

    transition:
        transform .25s ease,
        box-shadow .25s ease,
        background .25s ease;
}


.brand-button:hover {

    transform:
        translateY(-3px);

    background: #ffffff;

    box-shadow:
        0 14px 28px
        rgba(50,40,30,.13);
}


.brand-button:active {

    transform:
        scale(.97);
}


.brand-small {

    display: block;

    margin-top: 4px;

    font-size: 10px;

    font-weight: 600;

    color: #a0938b;
}


/* =========================================================
   เลือกหมวดหมู่อีกครั้ง

   *** อยู่ใน POPUP เท่านั้น ***
========================================================= */

.popup-choose-again {

    display: block;

    margin:
        26px auto 0;

    padding:
        10px 18px;

    border: 0;

    background: transparent;

    color: #786c65;

    cursor: pointer;

    font-size: 13px;

    font-weight: 850;

    text-decoration:
        underline;

    text-decoration-thickness: 1px;

    text-underline-offset: 5px;

    transition:
        color .25s ease,
        transform .25s ease;
}


.popup-choose-again:hover {

    color: #d45b38;

    transform:
        translateY(-2px);
}


/* =========================================================
   GLASS BREAK EFFECT
========================================================= */

.shards {

    position: absolute;

    inset: 0;

    z-index: 200;

    pointer-events: none;

    overflow: hidden;
}


.shard {

    position: absolute;

    width: 22px;
    height: 30px;

    opacity: 0;

    background:

        linear-gradient(
            135deg,
            rgba(255,255,255,.94),
            rgba(220,210,205,.16)
        );

    border:
        1px solid
        rgba(255,255,255,.90);

    clip-path:
        polygon(
            50% 0%,
            100% 35%,
            72% 100%,
            0% 68%
        );
}


.popup-layer.breaking
.shard {

    animation:
        glassBreak .72s
        cubic-bezier(.1,.8,.2,1)
        forwards;
}


@keyframes glassBreak {

    0% {

        opacity: 0;

        transform:
            translate(0,0)
            rotate(0)
            scale(.2);
    }

    20% {

        opacity: 1;
    }

    100% {

        opacity: 0;

        transform:
            translate(
                var(--x),
                var(--y)
            )
            rotate(var(--r))
            scale(var(--s));
    }
}


.shard:nth-child(1) {

    left: 35%;
    top: 40%;

    --x: -250px;
    --y: -170px;
    --r: -80deg;
    --s: 1.3;
}


.shard:nth-child(2) {

    left: 48%;
    top: 45%;

    --x: 280px;
    --y: -190px;
    --r: 110deg;
    --s: .8;
}


.shard:nth-child(3) {

    left: 54%;
    top: 42%;

    --x: 300px;
    --y: 160px;
    --r: 70deg;
    --s: 1.5;
}


.shard:nth-child(4) {

    left: 43%;
    top: 52%;

    --x: -320px;
    --y: 180px;
    --r: -130deg;
    --s: .9;
}


.shard:nth-child(5) {

    left: 50%;
    top: 50%;

    --x: -100px;
    --y: -260px;
    --r: 150deg;
    --s: .7;
}


.shard:nth-child(6) {

    left: 50%;
    top: 50%;

    --x: 90px;
    --y: 280px;
    --r: -70deg;
    --s: 1.2;
}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 1050px) {

    .category-grid {

        grid-template-columns:
            repeat(3, 1fr);

        overflow-y: auto;

        padding:
            20px 5px
            15px;
    }


    .category-card {

        height: 250px;
    }


    .icon-3d {

        width: 100px;
        height: 100px;

        font-size: 58px;
    }
}


@media (max-width: 700px) {

    .welcome-content {

        padding:
            30px 24px;
    }


    .brand {

        left: 24px;
        top: 28px;
    }


    .brand-name {

        font-size: 30px;
    }


    .brand-tagline {

        font-size: 14px;
    }


    .hero {

        max-width: 95%;

        font-size:
            clamp(48px, 15vw, 76px);

        letter-spacing: -3px;
    }


    .promo {

        font-size: 12px;

        padding:
            9px 14px;

        margin-bottom: 17px;
    }


    .description {

        max-width: 92%;

        margin-top: 21px;

        font-size: 14px;

        line-height: 1.55;
    }


    .bottom-note {

        left: 24px;

        bottom: 23px;

        font-size: 9px;
    }


    /* MOBILE ART */

    .ai-man {

        width: 180px;
        height: 360px;

        right: -30px;
        top: 18%;
    }


    .ai-dog-one {

        width: 190px;
        height: 220px;

        right: 24%;
        bottom: -15px;
    }


    .ai-dog-two {

        width: 160px;
        height: 190px;

        right: -20px;
        bottom: -5px;
    }


    .welcome-overlay {

        background:

            linear-gradient(
                180deg,
                rgba(255,251,247,.99) 0%,
                rgba(255,251,247,.94) 48%,
                rgba(255,251,247,.48) 100%
            );
    }


    /* PAGE 2 */

    .category-page {

        padding:
            22px 17px 18px;
    }


    .page-title {

        font-size: 32px;
    }


    .page-subtitle {

        font-size: 11px;
    }


    /* MOBILE VOUCHER */

    .voucher-button {

        padding:
            10px 14px;

        gap: 6px;

        font-size: 11px;
    }


    .truck-icon,
    .truck-icon svg {

        width: 17px;
        height: 17px;
    }


    /* CATEGORY */

    .category-grid {

        grid-template-columns:
            repeat(2, minmax(0, 1fr));

        gap: 11px;

        padding:
            20px 4px 10px;

        overflow-y: auto;
    }


    .category-card {

        height: 190px;

        border-radius: 23px;
    }


    .category-inner {

        padding: 14px;
    }


    .icon-3d {

        width: 78px;
        height: 78px;

        margin-top: 6px;

        border-radius: 22px;

        font-size: 45px;
    }


    .category-name {

        font-size: 13px;
    }


    .category-number {

        font-size: 9px;
    }


    /* TOUCH EFFECT */

    .category-card.touch-active {

        transform:
            scale(1.075)
            translateY(-5px);

        box-shadow:
            0 20px 40px
            rgba(45,35,28,.17);

        z-index: 30;
    }


    .category-grid.touching
    .category-card:not(.touch-active) {

        filter: blur(5px);

        opacity: .45;

        transform:
            scale(.97);
    }


    /* POPUP */

    .popup {

        width:
            calc(100% - 8px);

        max-height: 82vh;

        border-radius: 27px;

        padding:
            23px 18px;
    }


    .popup-title {

        font-size: 29px;
    }


    .popup-subtitle {

        font-size: 11px;
    }


    .brand-list {

        grid-template-columns: 1fr;

        gap: 9px;

        margin-top: 20px;
    }


    .brand-button {

        min-height: 56px;

        padding:
            12px 14px;

        font-size: 13px;
    }


    .popup-choose-again {

        margin-top: 20px;

        font-size: 12px;
    }
}


/* =========================================================
   REDUCED MOTION
========================================================= */

@media (prefers-reduced-motion: reduce) {

    .page,
    .category-card,
    .icon-3d,
    .popup,
    .popup-layer,
    .brand-button {

        transition: none !important;
    }

    .popup-layer.breaking
    .shard {

        animation: none !important;
    }
}

</style>
</head>


<body>

<div id="app">


<!-- =======================================================
     PAGE 1
======================================================= -->

<section
    id="page1"
    class="page"
>


    <div class="welcome-art">


        <!-- AI STYLE MAN -->

        <div
            class="ai-man"
            aria-hidden="true"
        ></div>


        <!-- CHIHUAHUA 1 -->

        <div
            class="ai-dog-one"
            aria-hidden="true"
        ></div>


        <!-- CHIHUAHUA 2 -->

        <div
            class="ai-dog-two"
            aria-hidden="true"
        ></div>


        <div class="welcome-overlay"></div>


    </div>



    <div class="welcome-content">


        <div class="brand">

            <div class="brand-name">
                all in me
            </div>

            <div class="brand-tagline">
                ชอบอยู่บ้าน
            </div>

        </div>



        <div>

            <div class="promo">
                โปรเด็ดลดแรง
            </div>


            <h1 class="hero">

                ช้อปง่าย

                <span class="hero-accent">
                    อยู่บ้านก็ฟิน
                </span>

            </h1>


            <p class="description">
                สินค้าจาก shopee mall ที่ผ่านการรองรับโดย shopee
                แนะนำจากเพจ all in me : ชอบอยู่บ้าน
            </p>

        </div>



        <div class="bottom-note">
            ALL IN ME • HOME LOVERS • SHOPEE MALL
        </div>


    </div>

</section>



<!-- =======================================================
     PAGE 2
======================================================= -->

<section
    id="page2"
    class="page"
>


    <div class="category-page">


        <div class="category-background"></div>



        <div class="category-content">


            <h2 class="page-title">
                เลือกหมวดหมู่
            </h2>


            <p class="page-subtitle">
                ชอบอะไร กดเลือกได้เลย
            </p>



            <!-- =================================================
                 ข้อ 15 — เก็บโค้ด
            ================================================== -->

            <button
                class="voucher-button"
                type="button"
                onclick="
                    openShopInNewTab(
                        'https://shopee.co.th/m/avc-fsv-all-vouchers'
                    )
                "
            >

                <span
                    class="truck-icon"
                    aria-hidden="true"
                >

                    <svg
                        viewBox="0 0 24 24"
                    >

                        <path
                            d="M3 6h11v10H3z"
                        />

                        <path
                            d="M14 10h4l3 3v3h-7z"
                        />

                        <circle
                            cx="7"
                            cy="18"
                            r="2"
                        />

                        <circle
                            cx="18"
                            cy="18"
                            r="2"
                        />

                        <path
                            d="M14 16h2"
                        />

                    </svg>

                </span>


                <span>
                    เก็บโค้ด
                </span>

            </button>



            <!-- =================================================
                 CATEGORY GRID

                 สำคัญ:
                 ไม่มี "เลือกหมวดหมู่อีกครั้ง" ตรงนี้
            ================================================== -->

            <main
                id="categoryGrid"
                class="category-grid"
            >


                <!-- PET -->

                <article
                    class="category-card"
                    data-category="pet"
                >

                    <div class="category-inner">

                        <div class="icon-3d">
                            🐶
                        </div>

                        <div class="category-name">
                            หมวดสัตว์เลี้ยง
                        </div>

                        <div class="category-number">
                            01
                        </div>

                    </div>

                </article>



                <!-- FOOD -->

                <article
                    class="category-card"
                    data-category="food"
                >

                    <div class="category-inner">

                        <div class="icon-3d">
                            🍜
                        </div>

                        <div class="category-name">
                            หมวดอาหาร
                        </div>

                        <div class="category-number">
                            02
                        </div>

                    </div>

                </article>



                <!-- HOUSEHOLD -->

                <article
                    class="category-card"
                    data-category="household"
                >

                    <div class="category-inner">

                        <div class="icon-3d">
                            🧺
                        </div>

                        <div class="category-name">
                            หมวดของใช้
                        </div>

                        <div class="category-number">
                            03
                        </div>

                    </div>

                </article>



                <!-- HOME DECOR -->

                <article
                    class="category-card"
                    data-category="decor"
                >

                    <div class="category-inner">

                        <div class="icon-3d">
                            🛋️
                        </div>

                        <div class="category-name">
                            หมวดหมู่ตกแต่งบ้าน
                        </div>

                        <div class="category-number">
                            04
                        </div>

                    </div>

                </article>



                <!-- SKINCARE -->

                <article
                    class="category-card"
                    data-category="skincare"
                >

                    <div class="category-inner">

                        <div class="icon-3d">
                            🧴
                        </div>

                        <div class="category-name">
                            หมวดหมู่สกินแคร์
                        </div>

                        <div class="category-number">
                            05
                        </div>

                    </div>

                </article>


            </main>

        </div>

    </div>

</section>



<!-- =======================================================
     BRAND POPUP

     สำคัญที่สุด:
     "เลือกหมวดหมู่อีกครั้ง"
     อยู่ตรงนี้เท่านั้น
======================================================= -->

<div
    id="popupLayer"
    class="popup-layer"
    aria-hidden="true"
>


    <!-- GLASS SHARDS -->

    <div class="shards">

        <span class="shard"></span>
        <span class="shard"></span>
        <span class="shard"></span>
        <span class="shard"></span>
        <span class="shard"></span>
        <span class="shard"></span>

    </div>



    <div
        class="popup"
        role="dialog"
        aria-modal="true"
    >


        <h3
            id="popupTitle"
            class="popup-title"
        >
            เลือกแบรนด์
        </h3>


        <p
            id="popupSubtitle"
            class="popup-subtitle"
        >
            เลือกร้านค้าที่ต้องการ
        </p>


        <div
            id="brandList"
            class="brand-list"
        ></div>



        <!-- =================================================
             ข้อ 9
             อยู่ใน POPUP เท่านั้น
             
             ไม่มี X
             ไม่มีลูกศร
        ================================================== -->

        <button
            id="chooseAgain"
            class="popup-choose-again"
            type="button"
        >
            เลือกหมวดหมู่อีกครั้ง
        </button>


    </div>

</div>



</div>


<script>

/* =========================================================
   SHOP DATA
========================================================= */

const shops = {


    pet: {

        title: "หมวดสัตว์เลี้ยง",

        brands: [

            {
                name: "Royal canin",
                url: "https://s.shopee.co.th/6L4leDd3Zm"
            },

            {
                name: "Pedigree",
                url: "https://s.shopee.co.th/3LRA4l8zOJ"
            },

            {
                name: "Jerhigh",
                url: "https://s.shopee.co.th/1gIw5jATDG"
            },

            {
                name: "Whiskas",
                url: "https://s.shopee.co.th/gQOxB5qGn"
            },

            {
                name: "SmartHeart & Me-O Official",
                url: "https://s.shopee.co.th/60RvJ1y0Vi"
            }

        ]

    },


    food: {

        title: "หมวดอาหาร",

        brands: [

            {
                name: "จะโหรม เครื่องแกงไทย",
                url: "https://s.shopee.co.th/1Lg5hOI8kW"
            },

            {
                name: "Ajinomoto",
                url: "https://s.shopee.co.th/9AOx1pqXpD"
            },

            {
                name: "Unilever",
                url: "https://s.shopee.co.th/9KiNEWYNVw"
            },

            {
                name: "Nestle Milk Official",
                url: "https://s.shopee.co.th/W6yjZC6ur"
            },

            {
                name: "Osotspa Delivery",
                url: "https://s.shopee.co.th/4LJhK7ZMdV"
            },

            {
                name: "Nguansoon_officia",
                url: "https://s.shopee.co.th/BU8MZrlEP"
            },

            {
                name: "ซอสปรุงรส ต่างๆ",
                url: "https://s.shopee.co.th/4fwXixy8Dg"
            }

        ]

    },


    household: {

        title: "หมวดของใช้",

        brands: [

            {
                name: "ถุงขยะ",
                url: "https://s.shopee.co.th/8Kpq39i085"
            },

            {
                name: "เครื่องครัว Tefal",
                url: "https://s.shopee.co.th/1qcMJLCWIL"
            },

            {
                name: "เครื่องใช้ไฟฟ้า Simplus group 1",
                url: "https://s.shopee.co.th/8AWPr4uRQg"
            },

            {
                name: "เครื่องใช้ไฟฟ้า Simplus group 2",
                url: "https://s.shopee.co.th/9pedqAnQUg"
            },

            {
                name: "เครื่องใช้ไฟฟ้า Seagull group 1",
                url: "https://s.shopee.co.th/AKauRED1KM"
            },

            {
                name: "เครื่องใช้ไฟฟ้า Seagull group 2",
                url: "https://s.shopee.co.th/2Vs36rbhc1"
            },

            {
                name: "เครื่องใช้ไฟฟ้า Camel",
                url: "https://s.shopee.co.th/9AOx3De0fv"
            },

            {
                name: "P&G Official Shop",
                url: "https://s.shopee.co.th/5AsoK81r7D"
            }

        ]

    },


    decor: {

        title: "หมวดหมู่ตกแต่งบ้าน",

        brands: [

            {
                name: "BARCO",
                url: "https://s.shopee.co.th/7fa9HJGPCR"
            },

            {
                name: "Index Living Mall Official",
                url: "https://s.shopee.co.th/40gqvptqWT"
            },

            {
                name: "Boonthavorn Official Store",
                url: "https://s.shopee.co.th/8AWPtZBDq0"
            },

            {
                name: "Dohome Shop Online",
                url: "https://s.shopee.co.th/1gIw9krZ7v"
            }

        ]

    },


    skincare: {

        title: "หมวดหมู่สกินแคร์",

        brands: [

            {
                name: "Smooth E Official Store",
                url: "https://s.shopee.co.th/6VOBshZnB9"
            },

            {
                name: "KAO Beauty & Personal Care",
                url: "https://s.shopee.co.th/1qcMKDKKtn"
            },

            {
                name: "Kose Official Store",
                url: "https://s.shopee.co.th/5fp4tL9I8a"
            },

            {
                name: "Unilever International",
                url: "https://s.shopee.co.th/1Ai8zfPs2"
            },

            {
                name: "NIVEA_Official_Store",
                url: "https://s.shopee.co.th/9pedrU1ai1"
            },

            {
                name: "Vaseline Official",
                url: "https://s.shopee.co.th/2Vs383wxOk"
            }

        ]

    }

};


/* =========================================================
   PAGE 1
   3 วินาที แล้วเลื่อนขึ้น
========================================================= */

window.addEventListener(
    "load",
    function() {

        setTimeout(
            function() {

                document.body.classList.add(
                    "entered"
                );

            },
            3000
        );

    }
);


/* =========================================================
   OPEN NEW TAB
========================================================= */

function openShopInNewTab(url) {

    window.open(
        url,
        "_blank",
        "noopener,noreferrer"
    );

}


/* =========================================================
   ELEMENTS
========================================================= */

const popupLayer =
    document.getElementById(
        "popupLayer"
    );


const popupTitle =
    document.getElementById(
        "popupTitle"
    );


const popupSubtitle =
    document.getElementById(
        "popupSubtitle"
    );


const brandList =
    document.getElementById(
        "brandList"
    );


const chooseAgain =
    document.getElementById(
        "chooseAgain"
    );


const categoryGrid =
    document.getElementById(
        "categoryGrid"
    );


const categoryCards =
    document.querySelectorAll(
        ".category-card"
    );


/* =========================================================
   OPEN BRAND POPUP
========================================================= */

function openBrandPopup(
    categoryKey
) {

    const category =
        shops[categoryKey];


    if (!category) {
        return;
    }


    popupTitle.textContent =
        category.title;


    popupSubtitle.textContent =
        "เลือกร้านค้าที่ต้องการ";


    brandList.innerHTML = "";


    category.brands.forEach(
        function(brand) {

            const button =
                document.createElement(
                    "button"
                );


            button.type =
                "button";


            button.className =
                "brand-button";


            button.innerHTML =
                `
                ${brand.name}

                <span class="brand-small">
                    เปิดร้านในแท็บใหม่
                </span>
                `;


            button.addEventListener(
                "click",
                function() {

                    openShopInNewTab(
                        brand.url
                    );

                }
            );


            brandList.appendChild(
                button
            );

        }
    );


    popupLayer.classList.remove(
        "breaking"
    );


    popupLayer.classList.add(
        "show"
    );


    popupLayer.setAttribute(
        "aria-hidden",
        "false"
    );

}


/* =========================================================
   CATEGORY CLICK
========================================================= */

categoryCards.forEach(
    function(card) {

        card.addEventListener(
            "click",
            function() {

                openBrandPopup(
                    this.dataset.category
                );

            }
        );

    }
);


/* =========================================================
   เลือกหมวดหมู่อีกครั้ง

   อยู่ใน POPUP เท่านั้น

   CLICK:
   → GLASS BREAK
   → CLOSE POPUP
   → CATEGORY PAGE ยังอยู่
========================================================= */

chooseAgain.addEventListener(
    "click",
    function() {

        popupLayer.classList.add(
            "breaking"
        );


        setTimeout(
            function() {

                popupLayer.classList.remove(
                    "show"
                );


                popupLayer.classList.remove(
                    "breaking"
                );


                popupLayer.setAttribute(
                    "aria-hidden",
                    "true"
                );

            },
            520
        );

    }
);


/* =========================================================
   BACKDROP
   ไม่ปิด popup
========================================================= */

popupLayer.addEventListener(
    "click",
    function(event) {

        if (
            event.target === popupLayer
        ) {

            event.stopPropagation();

        }

    }
);


/* =========================================================
   MOBILE TOUCH
========================================================= */

categoryCards.forEach(
    function(card) {


        card.addEventListener(
            "pointerdown",
            function() {

                categoryGrid.classList.add(
                    "touching"
                );


                this.classList.add(
                    "touch-active"
                );

            }
        );


        card.addEventListener(
            "pointerup",
            function() {

                this.classList.remove(
                    "touch-active"
                );


                setTimeout(
                    function() {

                        categoryGrid.classList.remove(
                            "touching"
                        );

                    },
                    250
                );

            }
        );


        card.addEventListener(
            "pointercancel",
            function() {

                this.classList.remove(
                    "touch-active"
                );


                categoryGrid.classList.remove(
                    "touching"
                );

            }
        );


        card.addEventListener(
            "pointerleave",
            function() {

                this.classList.remove(
                    "touch-active"
                );


                categoryGrid.classList.remove(
                    "touching"
                );

            }
        );

    }
);


/* =========================================================
   ESC
   ไม่ปิด POPUP
========================================================= */

document.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Escape"
        ) {

            event.preventDefault();

        }

    }
);

</script>

</body>
</html>
'''


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )