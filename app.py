from flask import Flask, render_template
import random

app = Flask(__name__)

sozler = [
    "Her sabit düşünce sahibi için zindandır.",
    "'Kendi iç evreninde düzen yoksa, dünyanın düzeninden şikâyet etmenin anlamı olmaz.",
    "Dışarıdaki olaylar değil, onlara dair yorumlarımız ruhumuzu sarsar; zihnini eğiten kişi, kaderle boğuşmaz.",
    "Absürdü fark eden kişi, umutsuzluğa değil berraklığa yaklaşır; anlamsızlık görülünce hayatın ağırlığı değil, dokusu değişir.",
    "İktidar, görünenden çok alışkanlıklarda saklanır; insan kendisini değil, kendisine öğretilmiş bakışları denetler",
    "Seçim yapmamak bile bir seçimdir; özgürlük insanın üzerinde taşıdığı en inatçı sorumluluktur."
    "Hayal gücü, haritaların gösterdiği sınırları kabul etmeyen tek ulaşım aracıdır."
]

@app.route('/')
def ana_sayfa():
    secilen_soz = random.choice(sozler)
    return render_template('index.html', soz=secilen_soz)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')