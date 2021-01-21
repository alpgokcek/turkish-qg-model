class QuestionPatterns:
    patterns = {
        "Asker": {
            "rütbesi": [
                "{name} hangi rütbede görev yapmaktaydı?",
                "{name}'{~}n rütbesi nedir?",
                "{name}'{~}n rütbesi",
                "{name}'{~}n rütbesi neydi?",
                "{name} rütbe",
                "{name} hangi rütbeye sahiptir?"
            ],
            "doğumyeri": [
                "{name} nerede doğmuştur?",
                "{name} nerede doğdu",
                "{name} doğum yeri",
                "{name}'{~}n doğum yeri",
                "{name} doğum yeri neresi",
                "{name}'{~}n doğum yeri neresi",
                "{name}'{~}n doğum yeri neresidir",
                "{name} doğum yeri neresidir",
                "{name} nereli",
                "{name} memleketi",
                "{name}'{~}n memleketi",
                "{name} memleketi nedir",
                "{name}'{~}n memleketi nedir",
                "{name} doğduğu yer",
                "{name}'{~}n doğduğu yer",
                "{name} doğduğu yer neresidir",
                "{name}'{~}n doğduğu yer neresidir",
                "{name} doğduğu yer neresi",
                "{name}'{~}n doğduğu yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n doğduğu il",
                "{name} hangi ilde doğdu",
                "{name} hangi ülkede doğdu",
                "{name} doğduğu ülke",
                "{name}'{~}n doğduğu ülke"
            ],
            "doğumtarihi": [
                "{name}'{~}n doğum tarihi",
                "{name}'{~}n doğum tarihi nedir",
                "{name}'{~}n doğum tarihi ne zaman",
                "{name}'{~}n doğum yılı",
                "{name}'{~}n doğum yılı nedir",
                "{name}'{~}n doğum yılı ne zaman",
                "{name}'{~}n doğum günü ne zaman",
                "{name}'{~}n doğum günü nedir",
                "{name} doğum tarihi",
                "{name} doğum tarihi nedir",
                "{name} doğum tarihi ne zaman",
                "{name} doğum yılı",
                "{name} doğum yılı nedir",
                "{name} doğum yılı ne zaman",
                "{name} doğum günü ne zaman",
                "{name} doğum günü nedir",
                "{name} ne zaman doğmuştur?",
                "{name} ne zaman doğdu",
                "{name} doğum zamanı"
            ],
            "hizmetyılları": [
                "{name}'{~}n hizmet yılları",
                "{name}'{~}n hizmet yılları nedir",
                "{name}'{~}n hizmet yılları ne zaman",
                "{name}'{~}n hizmet yılları ne zamandır",
                "{name}'{~}n ordudaki yılları",
                "{name}'{~}n ordudaki yılları nedir",
                "{name}'{~}n orduda geçirdiği yılları",
                "{name}'{~}n orduda geçirdiği yıllar",
                "{name} hizmet yılları",
                "{name} hizmet yılları nedir",
                "{name} hizmet yılları ne zaman",
                "{name} hizmet yılları ne zamandır",
                "{name} ordudaki yılları",
                "{name} ordudaki yılları nedir",
                "{name} orduda geçirdiği yılları",
                "{name} orduda geçirdiği yıllar",
                "{name} ne zaman hizmet vermiştir",
                "{name} ne zamanlar hizmet vermiştir",
                "{name} ne zaman hizmet vermişti",
                "{name} ne zamanlar hizmet vermişti",
                "{name} ne zaman askerdi",
                "{name} ne zaman asker olarak görev yapmıştır",
                "{name} ne zaman hizmet vermiştir",
                "{name} orduda geçirdiği yıllar",
                "{name} hangi yıllarını orduda geçirdi",
                "{name} hangi yıllarda ordudaydı",
                "{name} hangi yıllarda askerdi",
                "{name} hangi yıllarda arasında askerdi",
                "{name} hizmet dönemi",
                "{name} askerlik dönemi",
                "{name} ordu dönemi",
                "{name} ordudaki dönemi",
                "{name} ne zaman ordudaydı"
            ],
            "bağlılığı": [
                "{name} hangi ordudaydı",
                "{name} hangi orduda görev aldı",
                "{name} hangi orduya bağlı",
                "{name} hangi orduya bağlıydı",
                "{name} hangi orduya bağlıdır",
                "{name} hangi orduya bağlı görev aldı",
                "{name} hangi orduya bağlı görev almıştır",
                "{name} hangi ülke ordusundadır",
                "{name} hangi ülke ordusundaydı",
                "{name} hangi ülkenin ordusundaydı"
            ],
            "ölümyeri": [
                "{name} nerede ölmüştür",
                "{name} nerede öldü",
                "{name} ölüm yeri",
                "{name}'{~}n ölüm yeri",
                "{name} ölüm yeri neresi",
                "{name}'{~}n ölüm yeri neresi",
                "{name}'{~}n ölüm yeri neresidir",
                "{name} ölüm yeri neresidir",
                "{name} öldüğü yer",
                "{name}'{~}n öldüğü yer",
                "{name} öldüğü yer neresidir",
                "{name}'{~}n öldüğü yer neresidir",
                "{name} öldüğü yer neresi",
                "{name}'{~}n ölüdüğü yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n ölüdüğü il",
                "{name} hangi ilde öldü",
                "{name} hangi ülkede öldü",
                "{name} öldüğü ülke",
                "{name}'{~}n öldüğü ülke"
            ],
            "savaşları": [
                "{name} nerede savaştı",
                "{name} nerelerde savaştı",
                "{name} hangi cephelerde savaştı",
                "{name} hangi savaşlarda savaştı",
                "{name} hangi savaşlarda vardı",
                "{name} hangi savaşlardaydı",
                "{name} hangi savaşlara katıldı",
                "{name}'{~}n katıldığı savaşlar",
                "{name} katıldığı savaşlar",
                "{name} bulunduğu savaşlar",
                "{name}'{~}n bulunduğu savaşlar",
                "{name} savaşlar",
                "{name}'{~}n savaşlar",
                "{name} savaşları",
                "{name}'{~}n savaşları",
                "{name} savaştığı yerler",
                "{name}'{~}n savaştığı yerler",
                "{name}'{~}n savaştığı yerler neresi",
                "{name}'{~}n savaştığı yerler hangiler",
                "{name}'{~}n savaştığı yerler hangileridir",
                "{name}'{~}n savaştığı yerler hangileriydi",
                "{name}'{~}n savaştığı yer hangileriydi",
                "{name}'{~}n savaştığı yer hangileri"
            ],
            "ölümtarihi": [
                "{name}'{~}n ölüm tarihi",
                "{name}'{~}n ölüm tarihi nedir",
                "{name}'{~}n ölüm tarihi ne zaman",
                "{name}'{~}n ölüm yılı",
                "{name}'{~}n ölüm yılı nedir",
                "{name}'{~}n ölüm yılı ne zaman",
                "{name}'{~}n ölüm günü ne zaman",
                "{name}'{~}n ölüm günü nedir",
                "{name} ölüm tarihi",
                "{name} ölüm tarihi nedir",
                "{name} ölüm tarihi ne zaman",
                "{name} ölüm yılı",
                "{name} ölüm yılı nedir",
                "{name} ölüm yılı ne zaman",
                "{name} ölüm günü ne zaman",
                "{name} ölüm günü nedir",
                "{name} ne zaman ölmüştür",
                "{name} ne zaman ölüm",
                "{name} ölüm zamanı",
                "{name}'{~}n ölüm zamanı"
            ],
            "komutaettikleri": [
                "{name}'{~}n komuta ettikleri",
                "{name} komuta ettikleri",
                "{name} kimleri komuta etti",
                "{name} kimleri komuta etmiştir",
                "{name} altındaki askerler"
                "{name} komuta altındaki askerler"
                "{name}'{~}n komutası altındaki askerler"
                "{name} altındaki askerler"
            ],
            "madalya": [
                "{name} hangi madalyalara sahiptir?",
                "{name} hangi madalyaları almıştır?",
                "{name} aldığı madalyalar",
                "{name} sahip olduğu madalyalar nelerdir?",
                "{name}'{#} takdim edilen madalyalar nelerdir?",
                "{name}'{#} verilen madalyalar nelerdir?",
                "{name}'{~}n kazandığı madalyalar nelerdir?",
                "{name}'{~}n sahip olduğu madalyalar nelerdir?"
            ]
        },
         "Basketbolcu": {
             "pozisyon": [
                 "{name} hangi pozisyonda oynamaktadır?",
                 "{name} hangi pozisyonda oynar?",
                 "{name} hangi pozisyonda oynuyor?",
                 "{name} hangi mevkiide oynamaktadır?",
                 "{name} hangi mevkiide oynar?",
                 "{name} hangi mevkiide oynuyor?",
                 "{name}'{~}n oynadığı pozisyon nedir?",
                 "{name}'{~}n oynamakta olduğu pozisyon nedir?",
                 "{name}'{~}n pozisyonu nedir?",
                 "{name}'{~}n oyun pozisyonu nedir?",
                 "{name}'{~}n maçlardaki pozisyonu nedir?"
             ],
             "doğumtarihi": [
                 "{name}'{~}n doğum tarihi",
                 "{name}'{~}n doğum tarihi nedir",
                 "{name}'{~}n doğum tarihi ne zaman",
                 "{name}'{~}n doğum yılı",
                 "{name}'{~}n doğum yılı nedir",
                 "{name}'{~}n doğum yılı ne zaman",
                 "{name}'{~}n doğum günü ne zaman",
                 "{name}'{~}n doğum günü nedir",
                 "{name} doğum tarihi",
                 "{name} doğum tarihi nedir",
                 "{name} doğum tarihi ne zaman",
                 "{name} doğum yılı",
                 "{name} doğum yılı nedir",
                 "{name} doğum yılı ne zaman",
                 "{name} doğum günü ne zaman",
                 "{name} doğum günü nedir",
                 "{name} ne zaman doğmuştur?",
                 "{name} ne zaman doğdu",
                 "{name} doğum zamanı"
             ],
             "doğumyeri": [
                 "{name} nerede doğmuştur?",
                 "{name} nerede doğdu",
                 "{name} doğum yeri",
                 "{name}'{~}n doğum yeri",
                 "{name} doğum yeri neresi",
                 "{name}'{~}n doğum yeri neresi",
                 "{name}'{~}n doğum yeri neresidir",
                 "{name} doğum yeri neresidir",
                 "{name} nereli",
                 "{name} memleketi",
                 "{name}'{~}n memleketi",
                 "{name} memleketi nedir",
                 "{name}'{~}n memleketi nedir",
                 "{name} doğduğu yer",
                 "{name}'{~}n doğduğu yer",
                 "{name} doğduğu yer neresidir",
                 "{name}'{~}n doğduğu yer neresidir",
                 "{name} doğduğu yer neresi",
                 "{name}'{~}n doğduğu yer neresi",
                 "{name} doğduğu il",
                 "{name}'{~}n doğduğu il",
                 "{name} hangi ilde doğdu",
                 "{name} hangi ülkede doğdu",
                 "{name} doğduğu ülke",
                 "{name}'{~}n doğduğu ülke"
             ],
             "takım1": [
                 "{name}'{~}n ilk oynadığı takım hangisidir?",
                 "{name}'{~}n oynadığı ilk takım hangisidir?",
                 "{name}'{~}n ilk takımı hangisi?",
                 "{name}'{~}n ilk takımı hangisidir?",
                 "{name}'{~}n kariyerine başladığı takım hangisidir?",
                 "{name}'{~}n kariyerindeki ilk takım hangisidir?",
                 "{name} profesyonel kariyerine hangi takımda başlamıştır?",
                 "{name} profesyonel kariyerine hangi takımla başlamıştır?",
                 "{name} profesyonel kariyerine hangi takımla adım atmıştır?",
                 "{name}'{~}n profesyonel kariyerindeki ilk takım hangisidir?",
                 "{name}'{~}n profesyonel kariyerindeki ilk takım hangisiydi?",
                 "{name}'{~}n profesyonel kariyerindeki ilk takım hangisi?",
                 "{name}'{~}n profesyonel kariyerindeki ilk takım neydi?",
                 "{name}'{~}n profesyonel kariyerindeki ilk takım nedir?"
             ],
             "takımyıl1": [
                 "{name} profesyonel kariyerine ne zaman başlamıştır?",
                 "{name}'{~}n profesyonel kariyerine başlangıcı ne zamandır?",
                 "{name}'{~}n profesyonel kariyerine başlangıcı ne zamandı",
                 "{name}'{~}n profesyonel kariyerine başlangıcı ne zaman",
                 "{name}'{~}n profesyonel kariyerine başlangıcı ne zaman oldu?",
                 "{name}'{~}n profesyonel kariyerine başlangıcı ne zaman olmuştur?",
                 "{name} profesyonel kariyerine hangi yılda başladı?",
                 "{name} profesyonel kariyerine hangi yılda başlamıştı?",
                 "{name} profesyonel kariyerine hangi yılda başlamıştır?",
                 "{name} profesyonel kariyerine ne zaman başladı?",
                 "{name} profesyonel kariyerine ne zaman başlamıştı?",
                 "{name} profesyonel kariyerine ne zaman başlamıştır?",
                 "{name}'{~}n ilk takımında ne zaman oynamıştır?",
                 "{name}'{~}n ilk takımında ne zamanlar oynamıştır?",
                 "{name}'{~}n ilk takımında hangi yıllar oynamıştır?",
                 "{name}'{~}n ilk takımında hangi yıllar oynadı?",
                 "{name}'{~}n ilk takımında oynadığı zaman aralığı nedir?",
                 "{name}'{~}n ilk takımında oynadığı zaman aralığı nedir?",
                 "{name}'{~}n ilk oynadığı takımda ne zaman oynamıştır?",
                 "{name}'{~}n ilk oynadığı takımda hangi yıllar arasında oynamıştır?",
                 "{name}'{~}n ilk oynadığı takımda hangi yıllar arasında oynamıştı?",
                 "{name}'{~}n ilk oynadığı takımda hangi yıllar arasında oynadı?"
             ],
             "takım2": [
                 "{name}'{~}n ikinci oynadığı takım hangisidir?",
                 "{name}'{~}n oynadığı ikinci takım hangisidir?",
                 "{name}'{~}n oynadığı ikinci takım nedir?",
                 "{name}'{~}n oynadığı ikinci takımı ne",
                 "{name}'{~}n ikinci takımı nedir?",
                 "{name}'{~}n ikinci takımı hangisi?",
                 "{name}'{~}n ikinci takımı hangisidir?",
                 "{name}'{~}n kariyerindeki ikinci takım hangisidir?",
                 "{name}'{~}n kariyerindeki ikinci takım nedir?",
                 "{name}'{~}n profesyonel kariyerindeki ikinci takım hangisidir?",
                 "{name}'{~}n profesyonel kariyerindeki ikinci takım hangisiydi?",
                 "{name}'{~}n profesyonel kariyerindeki ikinci takım hangisi?",
                 "{name}'{~}n profesyonel kariyerindeki ikinci takım neydi?",
                 "{name}'{~}n profesyonel kariyerindeki ikinci takım nedir?"
             ],
             "takımyıl2": [
                 "{name}'{~}n ikinci takımında ne zaman oynamıştır?",
                 "{name}'{~}n ikinci takımında ne zamanlar oynamıştır?",
                 "{name} ikinci takımında hangi yıllar oynamıştır?",
                 "{name} ikinci takımında hangi yıllar oynadı?",
                 "{name}'{~}n ikinci takımında oynadığı zaman aralığı nedir?",
                 "{name} ikinci takımında oynadığı zaman aralığı nedir?",
                 "{name}'{~}n ikinci oynadığı takımda ne zaman oynamıştır?",
                 "{name} ikinci oynadığı takımda ne zaman oynamıştır?",
                 "{name}'{~}n ikinci oynadığı takımda hangi yıllar arasında oynamıştır?",
                 "{name}'{~}n ikinci oynadığı takımda hangi yıllar arasında oynamıştı?",
                 "{name}'{~}n ikinci oynadığı takımda hangi yıllar arasında oynadı?",
                 "{name}'{~}n oynadığı ikinci takımda hangi yıllar arasında oynadı?",
                 "{name}'{~}n oynadığı ikinci takımda hangi yıllar arasında oynamıştır?",
                 "{name}'{~}n oynadığı ikinci takımda hangi yıllar arasında oynamıştı?",
                 "{name}'{~}n oynadığı ikinci takımda hangi periyotta oynamıştı?",
                 "{name}'{~}n oynadığı ikinci takımda hangi periyotta oynamıştır?"
             ],
             "takım": [
                 "{name} hangi takımda oynamaktadır?",
                 "{name} şu an hangi takımda oynamaktadır?",
                 "{name} hangi takımda oynuyor?",
                 "{name} şu an hangi takımda oynuyor?",
                 "{name} hangi takımın oyuncusudur?",
                 "{name} şu an hangi takımın oyuncusudur?",
                 "{name} hangi takımdadır?",
                 "{name} şu an hangi takımdadır?",
                 "{name}'{~}n oynadığı takım hangisidir?",
                 "{name}'{~}n takımı hangisidir?",
                 "{name}'{~}n güncel takımı hangisidir?",
                 "{name}'{~}n şu an oynadığı takım hangisidir?"
             ],
             "lig": [
                 "{name} hangi ligde oynamaktadır?",
                 "{name} hangi ligde oynadı?",
                 "{name} şu an hangi ligde oynamaktadır?",
                 "{name} hangi ligde oynuyor?",
                 "{name} şu an hangi ligde oynuyor?",
                 "{name} hangi ligin oyuncusudur?",
                 "{name} şu an hangi ligin oyuncusudur?",
                 "{name} hangi ligdedir?",
                 "{name} şu an hangi ligdedir?",
                 "{name}'{~}n oynadığı lig hangisidir?",
                 "{name}'{~}n ligi hangisidir?",
                 "{name}'{~}n güncel ligi hangisidir?",
                 "{name}'{~}n şu an oynadığı takım hangisidir?"
             ]
         },
         "Bilim adamı": {
             "doğumyeri": [
                 "{name} nerede doğmuştur?",
                 "{name} nerede doğdu",
                 "{name} doğum yeri",
                 "{name}'{~}n doğum yeri",
                 "{name} doğum yeri neresi",
                 "{name}'{~}n doğum yeri neresi",
                 "{name}'{~}n doğum yeri neresidir",
                 "{name} doğum yeri neresidir",
                 "{name} nereli",
                 "{name} memleketi",
                 "{name}'{~}n memleketi",
                 "{name} memleketi nedir",
                 "{name}'{~}n memleketi nedir",
                 "{name} doğduğu yer",
                 "{name}'{~}n doğduğu yer",
                 "{name} doğduğu yer neresidir",
                 "{name}'{~}n doğduğu yer neresidir",
                 "{name} doğduğu yer neresi",
                 "{name}'{~}n doğduğu yer neresi",
                 "{name} doğduğu il",
                 "{name}'{~}n doğduğu il",
                 "{name} hangi ilde doğdu",
                 "{name} hangi ülkede doğdu",
                 "{name} doğduğu ülke",
                 "{name}'{~}n doğduğu ülke"
             ],
             "doğumtarihi": [
                 "{name}'{~}n doğum tarihi",
                 "{name}'{~}n doğum tarihi nedir",
                 "{name}'{~}n doğum tarihi ne zaman",
                 "{name}'{~}n doğum yılı",
                 "{name}'{~}n doğum yılı nedir",
                 "{name}'{~}n doğum yılı ne zaman",
                 "{name}'{~}n doğum günü ne zaman",
                 "{name}'{~}n doğum günü nedir",
                 "{name} doğum tarihi",
                 "{name} doğum tarihi nedir",
                 "{name} doğum tarihi ne zaman",
                 "{name} doğum yılı",
                 "{name} doğum yılı nedir",
                 "{name} doğum yılı ne zaman",
                 "{name} doğum günü ne zaman",
                 "{name} doğum günü nedir",
                 "{name} ne zaman doğmuştur?",
                 "{name} ne zaman doğdu",
                 "{name} doğum zamanı"
             ],
             "ölümyeri": [
                 "{name} nerede ölmüştür",
                 "{name} nerede öldü",
                 "{name} ölüm yeri",
                 "{name}'{~}n ölüm yeri",
                 "{name} ölüm yeri neresi",
                 "{name}'{~}n ölüm yeri neresi",
                 "{name}'{~}n ölüm yeri neresidir",
                 "{name} ölüm yeri neresidir",
                 "{name} öldüğü yer",
                 "{name}'{~}n öldüğü yer",
                 "{name} öldüğü yer neresidir",
                 "{name}'{~}n öldüğü yer neresidir",
                 "{name} öldüğü yer neresi",
                 "{name}'{~}n ölüdüğü yer neresi",
                 "{name} doğduğu il",
                 "{name}'{~}n ölüdüğü il",
                 "{name} hangi ilde öldü",
                 "{name} hangi ülkede öldü",
                 "{name} öldüğü ülke",
                 "{name}'{~}n öldüğü ülke"
             ],
             "ölümtarihi": [
                 "{name}'{~}n ölüm tarihi",
                 "{name}'{~}n ölüm tarihi nedir",
                 "{name}'{~}n ölüm tarihi ne zaman",
                 "{name}'{~}n ölüm yılı",
                 "{name}'{~}n ölüm yılı nedir",
                 "{name}'{~}n ölüm yılı ne zaman",
                 "{name}'{~}n ölüm günü ne zaman",
                 "{name}'{~}n ölüm günü nedir",
                 "{name} ölüm tarihi",
                 "{name} ölüm tarihi nedir",
                 "{name} ölüm tarihi ne zaman",
                 "{name} ölüm yılı",
                 "{name} ölüm yılı nedir",
                 "{name} ölüm yılı ne zaman",
                 "{name} ölüm günü ne zaman",
                 "{name} ölüm günü nedir",
                 "{name} ne zaman ölmüştür",
                 "{name} ne zaman ölüm",
                 "{name} ölüm zamanı",
                 "{name}'{~}n ölüm zamanı"
             ],
             "milliyeti": [
                 "{name} nerelidir?",
                 "{name} hangi ülke asıllıdır?",
                 "{name} hangi millettendir?",
                 "{name}'{~}n hangi millettendir?"
             ],
             "çalıştığıyerler": [
                 "{name}'{~}n çalıştığı yerler nedir?"
                 "{name}'{~}n çalıştığı yerler nerelerdir?"
                 "{name} nerelerde çalışmıştır?"
                 "{name} nerelerde çalıştı?"
                 "{name} nerelerde çalışmıştı?"
                 "{name}'{~}n çalıştığı kurumlar"
                 "{name}'{~}n çalıştığı kurumlar nerelerdir?"
                 "{name} hangi kurumlarda çalışmıştır?"
                 "{name}'{~}n çalıştığı kurumlar nedir?"
             ],
            "ödüller": [
                "{name} hangi ödüllere sahiptir?",
                "{name} hangi ödülleri almıştır?",
                "{name} aldığı ödüller",
                "{name} sahip olduğu ödüller nelerdir?",
                "{name}'{#} takdim edilen ödüller nelerdir?",
                "{name}'{#} verilen ödüller nelerdir?",
                "{name}'{~}n kazandığı ödüller nelerdir?",
                "{name}'{~}n sahip olduğu ödüller nelerdir?"
            ],
            "önemlibaşarıları": [
                "{name}'{~}n önemli başarıları nelerdir?"
                "{name}'{~}n sahip olduğu önemli başarılar nelerdir?"
                "{name}'{~}n elde ettiği önemli başarılar nelerdir?"
                "{name}'{~}n en önemli başarıları nelerdir?"
                "{name} en önemli başarıları nelerdir?"
            ],
             "vatandaşlığı": [
                 "{name} hangi ülke vatandaşıdır?",
                 "{name} hangi ülkenin vatandaşıdır?",
                 "{name} nerenin vatandaşıdır?",
                 "{name} vatandaşlığı hangi ülkedendir?",
                 "{name}'{~}n vatandaşlığı hangi ülkedendir?",
                 "{name}'{~}n vatandaşı olduğu ülke hangisidir?",
                 "{name}'{~}n vatandaşı olduğu ülke nedir?",
                 "{name}'{~}n vatandaşlığına sahip olduğu ülke nedir?",
                 "{name}'{~}n vatandaşlığına sahip olduğu ülke hangisidir?"
             ]
         },
         "Buz patencisi": {
             "ülke": [
                 "{name} hangi ülke vatandaşıdır?",
                 "{name} hangi ülke adına mücadele etmektedir?",
                 "{name} hangi ülkenin sporcusudur?",
                 "{name} hangi ülkenin sporcusuydu?",
                 "{name} hangi ülkenin sporcusu",
                 "{name} hangi ülkenin vatandaşıdır?",
                 "{name} nerenin vatandaşıdır?",
                 "{name} vatandaşlığı hangi ülkedendir?",
                 "{name}'{~}n vatandaşlığı hangi ülkedendir?",
                 "{name}'{~}n vatandaşı olduğu ülke hangisidir?",
                 "{name}'{~}n vatandaşı olduğu ülke nedir?",
                 "{name}'{~}n vatandaşlığına sahip olduğu ülke nedir?",
                 "{name}'{~}n vatandaşlığına sahip olduğu ülke hangisidir?"
             ],
             "koç": [
                 "{name}'{~}n koçu kimdir?",
                 "{name}'{~}n koçu kim?",
                 "{name}'{~}n koçu kimdi?",
                 "{name}'{~}n spor koçu kimdi?"
             ],

         },
         "Filozof": {},
         "Futbolcu": {},
         "Güreşçi": {},
         "Hakem": {},
         "Kişi": {},
         "Kraliyet": {},
         "Makam sahibi": {},
         "Manken": {},
         "Müzik sanatçısı": {
             "artalan": [
                "{name}'{~}n art alanı nedir?",
                "{name}'{~}n art alanı ne"
            ],
            "tarz":[
                "{name} hangi tür müzik yapar?",
                "{name} hangi tür müzik yaptı?",
                "{name} hangi tür müzik yapmaktadır?",
                "{name}'{~}n hangi tarzda müzik yapmaktadır?",
                "{name}'{~}n hangi tarzda müzik yapmakta",
                "{name}'{~}n hangi tarzda müzik yapar?",
                "{name}'{~}n hangi tarzlarda müzik yapmaktadır?",
                "{name}'{~}n hangi tarzlarda müzik yapmakta",
                "{name}'{~}n hangi tarzlarda müzik yapar?",
                "{name}'{~}n ne tarzda müzik yapmaktadır?",
                "{name}'{~}n ne tarzda müzik yapmaktadır?",
                "{name}'{~}n ne tarzda müzik yapar?",
                "{name}'{~}n ne tarzlarda müzik yapmaktadır?",
                "{name}'{~}n ne tarzlarda müzik yapmaktadır?",
                "{name}'{~}n ne tarzlarda müzik yapar?"
            ],
            "etkinyıllar":[
                "{name} hangi yıllarda aktif olarak müzik yapmıştır?",
                "{name} hangi yıllarda aktif olarak müzik yapmıştı?",
                "{name} hangi yıllarda aktif olarak müzik yapmıştır?"
            ],
            "meslek":[
                "{name}'{~}n mesleği",
                "{name}'{~}n mesleği nedir?",
                "{name}'{~}n mesleği ne",
                "{name}'{~}n mesleği neydi",
                "{name}'{~}n gerçek mesleği",
                "{name}'{~}n gerçek mesleği nedir?",
                "{name}'{~}n gerçek mesleği neydi"
            ],
            "plakşirketi":[

            ],
            "doğumadı":[

            ],
            "köken":[

            ],
            "yer":[

            ],
            "doğum":[

            ],
            "çalgı":[

            ]

         },
         "Oyuncu": {
             "yer": [
                
            ],
             "doğumtarihi": [
                "{name}'{~}n doğum tarihi",
                "{name}'{~}n doğum tarihi nedir",
                "{name}'{~}n doğum tarihi ne zaman",
                "{name}'{~}n doğum yılı",
                "{name}'{~}n doğum yılı nedir",
                "{name}'{~}n doğum yılı ne zaman",
                "{name}'{~}n doğum günü ne zaman",
                "{name}'{~}n doğum günü nedir",
                "{name} doğum tarihi",
                "{name} doğum tarihi nedir",
                "{name} doğum tarihi ne zaman",
                "{name} doğum yılı",
                "{name} doğum yılı nedir",
                "{name} doğum yılı ne zaman",
                "{name} doğum günü ne zaman",
                "{name} doğum günü nedir",
                "{name} ne zaman doğmuştur?",
                "{name} ne zaman doğdu",
                "{name} doğum zamanı"
            ],
            "meslek": [
                
            ],
            "etkinyılları": [
                
            ],
            "doğumadı": [
                
            ],
            "altyazı": [
                
            ],
            "evlilik": [
                
            ],
            "ulus": [
                
            ],
            "ölümtarihi": [
                "{name}'{~}n ölüm tarihi",
                "{name}'{~}n ölüm tarihi nedir",
                "{name}'{~}n ölüm tarihi ne zaman",
                "{name}'{~}n ölüm yılı",
                "{name}'{~}n ölüm yılı nedir",
                "{name}'{~}n ölüm yılı ne zaman",
                "{name}'{~}n ölüm günü ne zaman",
                "{name}'{~}n ölüm günü nedir",
                "{name} ölüm tarihi",
                "{name} ölüm tarihi nedir",
                "{name} ölüm tarihi ne zaman",
                "{name} ölüm yılı",
                "{name} ölüm yılı nedir",
                "{name} ölüm yılı ne zaman",
                "{name} ölüm günü ne zaman",
                "{name} ölüm günü nedir",
                "{name} ne zaman ölmüştür",
                "{name} ne zaman ölüm",
                "{name} ölüm zamanı",
                "{name}'{~}n ölüm zamanı"
            ],
            "ölümyeri": [
                "{name} nerede ölmüştür",
                "{name} nerede öldü",
                "{name} ölüm yeri",
                "{name}'{~}n ölüm yeri",
                "{name} ölüm yeri neresi",
                "{name}'{~}n ölüm yeri neresi",
                "{name}'{~}n ölüm yeri neresidir",
                "{name} ölüm yeri neresidir",
                "{name} öldüğü yer",
                "{name}'{~}n öldüğü yer",
                "{name} öldüğü yer neresidir",
                "{name}'{~}n öldüğü yer neresidir",
                "{name} öldüğü yer neresi",
                "{name}'{~}n ölüdüğü yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n ölüdüğü il",
                "{name} hangi ilde öldü",
                "{name} hangi ülkede öldü",
                "{name} öldüğü ülke",
                "{name}'{~}n öldüğü ülke"
            ]
         },
         "Profesyonel güreşçi": {
             "doğumyeri": [
                "{name} nerede doğmuştur?",
                "{name} nerede doğdu",
                "{name} doğum yeri",
                "{name}'{~}n doğum yeri",
                "{name} doğum yeri neresi",
                "{name}'{~}n doğum yeri neresi",
                "{name}'{~}n doğum yeri neresidir",
                "{name} doğum yeri neresidir",
                "{name} nereli",
                "{name} memleketi",
                "{name}'{~}n memleketi",
                "{name} memleketi nedir",
                "{name}'{~}n memleketi nedir",
                "{name} doğduğu yer",
                "{name}'{~}n doğduğu yer",
                "{name} doğduğu yer neresidir",
                "{name}'{~}n doğduğu yer neresidir",
                "{name} doğduğu yer neresi",
                "{name}'{~}n doğduğu yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n doğduğu il",
                "{name} hangi ilde doğdu",
                "{name} hangi ülkede doğdu",
                "{name} doğduğu ülke",
                "{name}'{~}n doğduğu ülke"
            ],
            "başlık": [
                
            ],
            "debut": [
                
            ],
            "doğumadı": [
                
            ],
            "doğumtarihi": [
                "{name}'{~}n doğum tarihi",
                "{name}'{~}n doğum tarihi nedir",
                "{name}'{~}n doğum tarihi ne zaman",
                "{name}'{~}n doğum yılı",
                "{name}'{~}n doğum yılı nedir",
                "{name}'{~}n doğum yılı ne zaman",
                "{name}'{~}n doğum günü ne zaman",
                "{name}'{~}n doğum günü nedir",
                "{name} doğum tarihi",
                "{name} doğum tarihi nedir",
                "{name} doğum tarihi ne zaman",
                "{name} doğum yılı",
                "{name} doğum yılı nedir",
                "{name} doğum yılı ne zaman",
                "{name} doğum günü ne zaman",
                "{name} doğum günü nedir",
                "{name} ne zaman doğmuştur?",
                "{name} ne zaman doğdu",
                "{name} doğum zamanı"
            ],
            "ringadları": [
                
            ],
            "eğiten": [
                
            ],
            "eş": [
                
            ],
            "eğitildiğiyer": [
                
            ],
            "çocuklar": [
                
            ]
         },
         "Sanatçı": {
             "doğumtarihi": [
                "{name}'{~}n doğum tarihi",
                "{name}'{~}n doğum tarihi nedir",
                "{name}'{~}n doğum tarihi ne zaman",
                "{name}'{~}n doğum yılı",
                "{name}'{~}n doğum yılı nedir",
                "{name}'{~}n doğum yılı ne zaman",
                "{name}'{~}n doğum günü ne zaman",
                "{name}'{~}n doğum günü nedir",
                "{name} doğum tarihi",
                "{name} doğum tarihi nedir",
                "{name} doğum tarihi ne zaman",
                "{name} doğum yılı",
                "{name} doğum yılı nedir",
                "{name} doğum yılı ne zaman",
                "{name} doğum günü ne zaman",
                "{name} doğum günü nedir",
                "{name} ne zaman doğmuştur?",
                "{name} ne zaman doğdu",
                "{name} doğum zamanı"
            ],
            "alanı": [
                
            ],
            "ölümtarihi": [
                "{name}'{~}n ölüm tarihi",
                "{name}'{~}n ölüm tarihi nedir",
                "{name}'{~}n ölüm tarihi ne zaman",
                "{name}'{~}n ölüm yılı",
                "{name}'{~}n ölüm yılı nedir",
                "{name}'{~}n ölüm yılı ne zaman",
                "{name}'{~}n ölüm günü ne zaman",
                "{name}'{~}n ölüm günü nedir",
                "{name} ölüm tarihi",
                "{name} ölüm tarihi nedir",
                "{name} ölüm tarihi ne zaman",
                "{name} ölüm yılı",
                "{name} ölüm yılı nedir",
                "{name} ölüm yılı ne zaman",
                "{name} ölüm günü ne zaman",
                "{name} ölüm günü nedir",
                "{name} ne zaman ölmüştür",
                "{name} ne zaman ölüm",
                "{name} ölüm zamanı",
                "{name}'{~}n ölüm zamanı"
            ],
            "ölümyeri": [
                "{name} nerede ölmüştür",
                "{name} nerede öldü",
                "{name} ölüm yeri",
                "{name}'{~}n ölüm yeri",
                "{name} ölüm yeri neresi",
                "{name}'{~}n ölüm yeri neresi",
                "{name}'{~}n ölüm yeri neresidir",
                "{name} ölüm yeri neresidir",
                "{name} öldüğü yer",
                "{name}'{~}n öldüğü yer",
                "{name} öldüğü yer neresidir",
                "{name}'{~}n öldüğü yer neresidir",
                "{name} öldüğü yer neresi",
                "{name}'{~}n ölüdüğü yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n ölüdüğü il",
                "{name} hangi ilde öldü",
                "{name} hangi ülkede öldü",
                "{name} öldüğü ülke",
                "{name}'{~}n öldüğü ülke"
            ],
            "doğumyeri": [
                "{name} nerede doğmuştur?",
                "{name} nerede doğdu",
                "{name} doğum yeri",
                "{name}'{~}n doğum yeri",
                "{name} doğum yeri neresi",
                "{name}'{~}n doğum yeri neresi",
                "{name}'{~}n doğum yeri neresidir",
                "{name} doğum yeri neresidir",
                "{name} nereli",
                "{name} memleketi",
                "{name}'{~}n memleketi",
                "{name} memleketi nedir",
                "{name}'{~}n memleketi nedir",
                "{name} doğduğu yer",
                "{name}'{~}n doğduğu yer",
                "{name} doğduğu yer neresidir",
                "{name}'{~}n doğduğu yer neresidir",
                "{name} doğduğu yer neresi",
                "{name}'{~}n doğduğu yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n doğduğu il",
                "{name} hangi ilde doğdu",
                "{name} hangi ülkede doğdu",
                "{name} doğduğu ülke",
                "{name}'{~}n doğduğu ülke"
            ],
            "milliyeti": [
                
            ],
            "yer": [
                
            ],
            "resimaltı": [
                
            ],
            "ünlüyapıtları": [
                
            ],
            "dogumadı": [
                
            ],
         },
         "Sporcu": {
             "doğumtarihi": [
                "{name}'{~}n doğum tarihi",
                "{name}'{~}n doğum tarihi nedir?",
                "{name}'{~}n doğum tarihi ne zaman",
                "{name}'{~}n doğum yılı",
                "{name}'{~}n doğum yılı nedir",
                "{name}'{~}n doğum yılı ne zaman",
                "{name}'{~}n doğum günü ne zaman",
                "{name}'{~}n doğum günü nedir",
                "{name} doğum tarihi",
                "{name} doğum tarihi nedir",
                "{name} doğum tarihi ne zaman",
                "{name} doğum yılı",
                "{name} doğum yılı nedir",
                "{name} doğum yılı ne zaman",
                "{name} doğum günü ne zaman",
                "{name} doğum günü nedir",
                "{name} ne zaman doğmuştur?",
                "{name} ne zaman doğdu",
                "{name} doğum zamanı"
            ],
             "doğumyeri": [
                "{name} nerede doğmuştur?",
                "{name} nerede doğdu",
                "{name} doğum yeri",
                "{name}'{~}n doğum yeri",
                "{name} doğum yeri neresi",
                "{name}'{~}n doğum yeri neresi",
                "{name}'{~}n doğum yeri neresidir",
                "{name} doğum yeri neresidir",
                "{name} nereli",
                "{name} memleketi",
                "{name}'{~}n memleketi",
                "{name} memleketi nedir",
                "{name}'{~}n memleketi nedir",
                "{name} doğduğu yer",
                "{name}'{~}n doğduğu yer",
                "{name} doğduğu yer neresidir",
                "{name}'{~}n doğduğu yer neresidir",
                "{name} doğduğu yer neresi",
                "{name}'{~}n doğduğu yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n doğduğu il",
                "{name} hangi ilde doğdu",
                "{name} hangi ülkede doğdu",
                "{name} doğduğu ülke",
                "{name}'{~}n doğduğu ülke"
            ],
            "ülke": [
                
            ],
            "spor": [
                
            ],
            "yarışma": [
                
            ],
            "uyruk": [
                
            ],
            "kei": [
                
            ],
            "resimaltı": [
                
            ],
            "ağırlık": [
                
            ],
            "ölümtarihi": [
                
            ],
         },
         "Tenis sporcu": {
             "doğumyeri": [
                "{name} nerede doğmuştur?",
                "{name} nerede doğdu",
                "{name} doğum yeri",
                "{name}'{~}n doğum yeri",
                "{name} doğum yeri neresi",
                "{name}'{~}n doğum yeri neresi",
                "{name}'{~}n doğum yeri neresidir",
                "{name} doğum yeri neresidir",
                "{name} nereli",
                "{name} memleketi",
                "{name}'{~}n memleketi",
                "{name} memleketi nedir",
                "{name}'{~}n memleketi nedir",
                "{name} doğduğu yer",
                "{name}'{~}n doğduğu yer",
                "{name} doğduğu yer neresidir",
                "{name}'{~}n doğduğu yer neresidir",
                "{name} doğduğu yer neresi",
                "{name}'{~}n doğduğu yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n doğduğu il",
                "{name} hangi ilde doğdu",
                "{name} hangi ülkede doğdu",
                "{name} doğduğu ülke",
                "{name}'{~}n doğduğu ülke"
            ],
            "vatandaşlık": [
                
            ],
            "enyükseksıralama": [
                
            ],
            "oyunstili": [
                
            ],
            "wimbledonsonuçları": [
                
            ],
            "amerikaaçıksonuçları": [
                
            ],
            "fransaaçıksonuçları": [
                
            ],
            "avustralyaaçıksonuçları": [
                
            ],
            "toplamkupa": [
                
            ],
            "yaşadığıyer": [
                
            ]
         },
         "Voleybolcu": {
             "doğumtarihi": [
                "{name}'{~}n doğum tarihi",
                "{name}'{~}n doğum tarihi nedir?",
                "{name}'{~}n doğum tarihi ne zaman",
                "{name}'{~}n doğum yılı",
                "{name}'{~}n doğum yılı nedir",
                "{name}'{~}n doğum yılı ne zaman",
                "{name}'{~}n doğum günü ne zaman",
                "{name}'{~}n doğum günü nedir",
                "{name} doğum tarihi",
                "{name} doğum tarihi nedir",
                "{name} doğum tarihi ne zaman",
                "{name} doğum yılı",
                "{name} doğum yılı nedir",
                "{name} doğum yılı ne zaman",
                "{name} doğum günü ne zaman",
                "{name} doğum günü nedir",
                "{name} ne zaman doğmuştur?",
                "{name} ne zaman doğdu",
                "{name} doğum zamanı"
            ],
            "doğumyeri": [
                "{name} nerede doğmuştur?",
                "{name} nerede doğdu",
                "{name} doğum yeri",
                "{name}'{~}n doğum yeri",
                "{name} doğum yeri neresi",
                "{name}'{~}n doğum yeri neresi",
                "{name}'{~}n doğum yeri neresidir",
                "{name} doğum yeri neresidir",
                "{name} nereli",
                "{name} memleketi",
                "{name}'{~}n memleketi",
                "{name} memleketi nedir",
                "{name}'{~}n memleketi nedir",
                "{name} doğduğu yer",
                "{name}'{~}n doğduğu yer",
                "{name} doğduğu yer neresidir",
                "{name}'{~}n doğduğu yer neresidir",
                "{name} doğduğu yer neresi",
                "{name}'{~}n doğduğu yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n doğduğu il",
                "{name} hangi ilde doğdu",
                "{name} hangi ülkede doğdu",
                "{name} doğduğu ülke",
                "{name}'{~}n doğduğu ülke"
            ],
             "pozisyon": [
                 "{name} hangi pozisyonda oynamaktadır?",
                 "{name} hangi pozisyonda oynar?",
                 "{name} hangi pozisyonda oynuyor?",
                 "{name} hangi mevkiide oynamaktadır?",
                 "{name} hangi mevkiide oynar?",
                 "{name} hangi mevkiide oynuyor?",
                 "{name}'{~}n oynadığı pozisyon nedir?",
                 "{name}'{~}n oynamakta olduğu pozisyon nedir?",
                 "{name}'{~}n pozisyonu nedir?",
                 "{name}'{~}n oyun pozisyonu nedir?",
                 "{name}'{~}n maçlardaki pozisyonu nedir?"
             ],
             "milliyeti": [
                 "{name} nerelidir?",
                 "{name} hangi ülke asıllıdır?",
                 "{name} hangi millettendir?",
                 "{name}'{~}n hangi millettendir?"
             ],
            "kulüpyıl": [
                
            ],
            "kulüptakım": [
                
            ],
            "bulunduğukulüp": [
                 "{name} hangi takımda oynamaktadır?",
                 "{name} şu an hangi takımda oynamaktadır?",
                 "{name} hangi takımda oynuyor?",
                 "{name} şu an hangi takımda oynuyor?",
                 "{name} hangi takımın oyuncusudur?",
                 "{name} şu an hangi takımın oyuncusudur?",
                 "{name} hangi takımdadır?",
                 "{name} şu an hangi takımdadır?",
                 "{name}'{~}n oynadığı takım hangisidir?",
                 "{name}'{~}n takımı hangisidir?",
                 "{name}'{~}n güncel takımı hangisidir?",
                 "{name}'{~}n şu an oynadığı takım hangisidir?"
             ],
            "numarası": [
                
            ],
            "millitakım": [
                
            ],
            "milliyıl": [
                
            ]

         },
         "Yazar": {
             "doğumyeri": [
                "{name} nerede doğmuştur?",
                "{name} nerede doğdu",
                "{name} doğum yeri",
                "{name}'{~}n doğum yeri",
                "{name} doğum yeri neresi",
                "{name}'{~}n doğum yeri neresi",
                "{name}'{~}n doğum yeri neresidir",
                "{name} doğum yeri neresidir",
                "{name} nereli",
                "{name} memleketi",
                "{name}'{~}n memleketi",
                "{name} memleketi nedir",
                "{name}'{~}n memleketi nedir",
                "{name} doğduğu yer",
                "{name}'{~}n doğduğu yer",
                "{name} doğduğu yer neresidir",
                "{name}'{~}n doğduğu yer neresidir",
                "{name} doğduğu yer neresi",
                "{name}'{~}n doğduğu yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n doğduğu il",
                "{name} hangi ilde doğdu",
                "{name} hangi ülkede doğdu",
                "{name} doğduğu ülke",
                "{name}'{~}n doğduğu ülke"
            ],
            "meslek": [
                "{name}'{~}n mesleği nedir?",
                "{name} mesleği nedir?",
                "{name} mesleği ne idi?",
                "{name} hangi mesleğe mensuptur?",
                "{name} hangi mesleğe mensup?",
                "{name} hangi mesleği yapıyordu?",
                "{name} hangi işi yapıyor?",
                "{name} hangi işi yapıyordu?"
            ],
             "doğumtarihi": [
                "{name}'{~}n doğum tarihi",
                "{name}'{~}n doğum tarihi nedir?",
                "{name}'{~}n doğum tarihi ne zaman",
                "{name}'{~}n doğum yılı",
                "{name}'{~}n doğum yılı nedir",
                "{name}'{~}n doğum yılı ne zaman",
                "{name}'{~}n doğum günü ne zaman",
                "{name}'{~}n doğum günü nedir",
                "{name} doğum tarihi",
                "{name} doğum tarihi nedir",
                "{name} doğum tarihi ne zaman",
                "{name} doğum yılı",
                "{name} doğum yılı nedir",
                "{name} doğum yılı ne zaman",
                "{name} doğum günü ne zaman",
                "{name} doğum günü nedir",
                "{name} ne zaman doğmuştur?",
                "{name} ne zaman doğdu",
                "{name} doğum zamanı"
            ],
            "ölümtarihi": [
                "{name}'{~}n ölüm tarihi",
                "{name}'{~}n ölüm tarihi nedir",
                "{name}'{~}n ölüm tarihi ne zaman",
                "{name}'{~}n ölüm yılı",
                "{name}'{~}n ölüm yılı nedir",
                "{name}'{~}n ölüm yılı ne zaman",
                "{name}'{~}n ölüm günü ne zaman",
                "{name}'{~}n ölüm günü nedir",
                "{name} ölüm tarihi",
                "{name} ölüm tarihi nedir",
                "{name} ölüm tarihi ne zaman",
                "{name} ölüm yılı",
                "{name} ölüm yılı nedir",
                "{name} ölüm yılı ne zaman",
                "{name} ölüm günü ne zaman",
                "{name} ölüm günü nedir",
                "{name} ne zaman ölmüştür",
                "{name} ne zaman ölüm",
                "{name} ölüm zamanı",
                "{name}'{~}n ölüm zamanı"
            ],
            "ölümyeri": [
                "{name} nerede ölmüştür",
                "{name} nerede öldü",
                "{name} ölüm yeri",
                "{name}'{~}n ölüm yeri",
                "{name} ölüm yeri neresi",
                "{name}'{~}n ölüm yeri neresi",
                "{name}'{~}n ölüm yeri neresidir",
                "{name} ölüm yeri neresidir",
                "{name} öldüğü yer",
                "{name}'{~}n öldüğü yer",
                "{name} öldüğü yer neresidir",
                "{name}'{~}n öldüğü yer neresidir",
                "{name} öldüğü yer neresi",
                "{name}'{~}n ölüdüğü yer neresi",
                "{name} doğduğu il",
                "{name}'{~}n ölüdüğü il",
                "{name} hangi ilde öldü",
                "{name} hangi ülkede öldü",
                "{name} öldüğü ülke",
                "{name}'{~}n öldüğü ülke"
            ],
            "başlık": [

            ],
            "tür": [
                "{name} hangi türde eser vermiştir?",
                "{name} hangi türde eserler vermiştir?",
                "{name} hangi türde yazmıştır?",
                "{name} hangi türde yazmaktaydır?",
                "{name}'{~}n eserleri hangi türdedir?",
                "{name}'{~}n eser türleri?",
                "{name}'{~}n eserleri hangi türdedir?",
                "{name}'{~}n eserleri hangi türdeydi?",
                "{name}'{~}n eser türü nedir?"
            ],
            "dönem": [
                "{name} hangi dönemde eser vermiştir?",
                "{name} hangi dönemde eserler vermiştir?",
                "{name} hangi dönem yazarıdır?",
                "{name} eser verdiği dönem nedir?",
                "{name} eser verdiği dönem hangisidir?"
            ],
            "ilkeser": [
                "{name}'{~}n ilk eseri nedir?",
                "{name}'{~}n ilk eseri hangisidir?",
                "{name}'{~}n ilk eseri?",
                "{name}'{~}n ilk eserinin adı nedir?",
                "{name}'{~}n verdiği ilk eserinin adı nedir?",
                "{name}'{~}n verdiği ilk eseri nedir?",
                "{name}'{~}n verdiği ilk eseri hangisidir?"
            ]
         }
    }