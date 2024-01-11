import cssutils

css_string = """
* { box-sizing: border-box; }
body { margin: 0; }
.titulo_portada {
    text-align: center;
    color: white;
    font-size: 90px;
    font-family: "Noto Serif Display";
    font-weight: 600;
    font-style: italic;
}
.image {
    position: absolute;
}
.top-right {
    top: 0px;
    right: 0px;
}
.bottom-left {
    bottom: 0px;
    left: 0px;
}
#portada-Western {
    background-image: url("http://localhost/invitacion-autenticacion/archivos/western.png");
    background-size: cover;
    background-position-x: center;
    background-position-y: center;
    background-repeat: no-repeat;
    height: 100vh;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: rgba(7, 7, 7, 0.3) 0px 0px 0px 2000px inset;
}
.image.bottom-left {
    width: 99px;
}
.image.top-right {
    width: 131px;
}
.texto_portada {
    text-align: center;
    font-size: 25px;
    letter-spacing: 6px;
    color: rgb(241, 241, 241);
}
@media (max-width: 480px) {
    .image.bottom-left {
        width: 75px;
        height: 270px;
    }
    .image.top-right {
        width: 109px;
        height: 269px;
    }
}
"""

parser = cssutils.CSSParser()
stylesheet = parser.parseString(css_string)

new_styles = []

for rule in stylesheet:
    if isinstance(rule, cssutils.css.cssstyledeclaration.CSSStyleDeclaration):
        selectors = rule.selectorList
        should_skip_rule = any(
            '*' in selector.selectorText or 'body' in selector.selectorText for selector in selectors)

        if not should_skip_rule:
            new_styles.append(rule.cssText)

new_css_string = '\n'.join(new_styles)
print(new_css_string)
