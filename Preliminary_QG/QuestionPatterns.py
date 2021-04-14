class QuestionPatterns:
    patterns = {
        "Asker": {
            "rütbesi": [
                "{name} hangi rütbede görev yapmaktaydı?",
                "{name}'{_suffix1} rütbesi nedir?",
                "{name}'{_suffix1} sahip olduğu rütbe nedir?",
                "{name} hangi rütbeye sahiptir?",
                "{name} ordudaki rütbesi nedir?"

            ],
            "hizmetyılları": [
                "{name}'{_suffix1} hizmet yılları nedir?",
                "{name}'{_suffix1} hizmet yılları ne zamandır?",
                "{name}'{_suffix1} ordudaki yılları nedir?",
                "{name}'{_suffix1} orduda geçirdiği yıllar nedir?",
                "{name}'{_suffix1} orduda bulunduğu yıllar nedir?",
                "{name} ne zaman hizmet vermiştir?",
                "{name} ne zaman orduda bulunmuştur?",
                "{name} ne zamanlar hizmet vermiştir?",
                "{name} ne zaman asker olarak görev yapmıştır?",
                "{name} hangi yıllar arasında hizmet vermiştir",
                "{name} hangi yıllar arasında orduda hizmet vermiştir?",
                "{name} hangi yıllar arasında orduda bulunmuştur?",
                "{name}'{_suffix1} orduda geçirdiği yıllar hangileridir?",
                "{name} hangi yıllarını orduda geçirmiştir?",
                "{name} hangi yıllarda orduda bulundu?",
                "{name} hangi yıllarda asker olarak görev yapmıştır?",
                "{name} hangi yıllarda arasında askerlik yapmaktaydı?",
            ],
            "bağlılığı": [
                "{name} hangi ordudaydı?",
                "{name} hangi orduda görev aldı?",
                "{name} hangi orduya bağlıdır?",
                "{name} hangi orduya bağlı görev aldı?",
                "{name} hangi orduya bağlı olarak görev almıştır?",
                "{name} hangi ülke ordusunda bulunuyordu?",
                "{name} hangi ülke ordusunda görev almıştır?",
                "{name} hangi ülke ordusuna mensuptur?",
                "{name}'{_suffix1} bağlı bulunduğu ordu hangisidir?"
                "{name}'{_suffix1} bağlılığı hangi ordudaydı?"
            ],
            "savaşları": [
                "{name} nerede savaşmıştır?",
                "{name} nerelerde savaşmıştır",
                "{name} hangi cephelerde savaştı?",
                "{name} hangi savaşlarda savaştı?",
                "{name} hangi savaşlara katılmıştır?",
                "{name}'{_suffix1} katıldığı savaşlar nelerdir?",
                "{name}'{_suffix1} bulunduğu savaşlar hangileriydi?",
            ],
            "komutaettikleri": [
                "{name}'{_suffix1} komuta ettikleri kimlerdir?",
                "{name}'{_suffix1} komuta ettiği askerler kimlerdi?",
                "{name} kimleri komuta etmiştir?",
                "{name}'{_suffix1} komutası altında kimler bulunuyordu?"
            ],
            "madalya": [
                "{name} hangi madalyalara sahiptir?",
                "{name} hangi madalyaları almıştır?",
                "{name}'{_suffix2} takdim edilen madalyalar nelerdir?",
                "{name}'{_suffix2} verilen madalyalar nelerdir?",
                "{name}'{_suffix1} kazandığı madalyalar hangileriydi?",
                "{name}'{_suffix1} sahip olduğu madalyalar nelerdir?"
            ]
        },
        "Basketbolcu": {
            "pozisyon": [
                "{name} hangi pozisyonda oynamaktadır?",
                "{name} hangi pozisyonda oynuyor?",
                "{name} hangi mevkiide oynamaktadır?",
                "{name} hangi mevkiide oynar?",
                "{name} hangi mevkiide oynuyor?",
                "{name}'{_suffix1} oynadığı pozisyon nedir?",
                "{name}'{_suffix1} oynamakta olduğu pozisyon nedir?",
                "{name}'{_suffix1} pozisyonu nedir?",
                "{name}'{_suffix1} oyun pozisyonu nedir?",
                "{name}'{_suffix1} maçlardaki pozisyonu nedir?"
            ],
            "takım1": [
                "{name}'{_suffix1} ilk oynadığı takım hangisidir?",
                "{name}'{_suffix1} oynadığı ilk takım hangisidir?",
                "{name}'{_suffix1} ilk takımı hangisi?",
                "{name}'{_suffix1} ilk takımı hangisidir?",
                "{name}'{_suffix1} kariyerine başladığı takım hangisidir?",
                "{name}'{_suffix1} kariyerindeki ilk takım hangisidir?",
                "{name} kariyerine hangi takımda başlamıştır?",
                "{name} profesyonel kariyerine hangi takımda başlamıştır?",
                "{name} profesyonel kariyerine hangi takımla başlamıştır?",
                "{name} profesyonel kariyerine hangi takımla adım atmıştır?",
                "{name}'{_suffix1} profesyonel kariyerindeki ilk takım hangisidir?",
                "{name}'{_suffix1} profesyonel kariyerindeki ilk takım hangisi?",
            ],
            "takımyıl1": [
                "{name} profesyonel kariyerine ne zaman başlamıştır?",
                "{name}'{_suffix1} profesyonel kariyerine başlangıcı ne zamandır?",
                "{name}'{_suffix1} profesyonel kariyerine başlangıcı ne zaman oldu?",
                "{name}'{_suffix1} profesyonel kariyerine başlangıcı ne zaman olmuştur?",
                "{name} profesyonel kariyerine hangi yılda başladı?",
                "{name} profesyonel kariyerine hangi yılda başlamıştır?",
                "{name} profesyonel kariyerine ne zaman başladı?",
                "{name} profesyonel kariyerine ne zaman başlamıştır?",
                "{name}'{_suffix1} ilk takımında ne zaman oynamıştır?",
                "{name}'{_suffix1} ilk takımında hangi yıllar oynamıştır?",
                "{name}'{_suffix1} ilk takımında hangi yıllar oynadı?",
                "{name}'{_suffix1} ilk takımında oynadığı zaman aralığı nedir?",
                "{name}'{_suffix1} ilk oynadığı takımda ne zaman oynamıştır?",
                "{name}'{_suffix1} ilk oynadığı takımda hangi yıllar arasında oynamıştır?",
                "{name}'{_suffix1} ilk oynadığı takımda hangi yıllar arasında oynamıştı?",
                "{name}'{_suffix1} ilk oynadığı takımda hangi yıllar arasında oynadı?"
            ],
            "takım2": [
                "{name}'{_suffix1} ikinci oynadığı takım hangisidir?",
                "{name}'{_suffix1} oynadığı ikinci takım hangisidir?",
                "{name}'{_suffix1} oynadığı ikinci takım nedir?",
                "{name}'{_suffix1} ikinci takımı nedir?",
                "{name}'{_suffix1} ikinci takımı hangisi?",
                "{name}'{_suffix1} ikinci takımı hangisidir?",
                "{name}'{_suffix1} kariyerindeki ikinci takım hangisidir?",
                "{name}'{_suffix1} kariyerindeki ikinci takım nedir?",
                "{name}'{_suffix1} profesyonel kariyerindeki ikinci takım hangisidir?",
                "{name}'{_suffix1} profesyonel kariyerindeki ikinci takım hangisiydi?",
                "{name}'{_suffix1} profesyonel kariyerindeki ikinci takım hangisi?",
                "{name}'{_suffix1} profesyonel kariyerindeki ikinci takım nedir?"
            ],
            "takımyıl2": [
                "{name} kariyerindeki ikinci takımda ne zaman oynamıştır?",
                "{name} ikinci takımında ne zaman oynamıştır?",
                "{name} ikinci takımında hangi yıllar oynamıştır?",
                "{name} ikinci takımında hangi yıllar oynadı?",
                "{name}'{_suffix1} ikinci takımında oynadığı zaman aralığı nedir?",
                "{name} ikinci oynadığı takımda hangi yıllar arasında oynamıştır?",
                "{name} oynadığı ikinci takımda hangi yıllar arasında oynadı?",
                "{name} oynadığı ikinci takımda hangi yıllar arasında oynamıştır?",
                "{name} oynadığı ikinci takımda hangi periyotta oynamıştır?"
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
                "{name}'{_suffix1} oynadığı takım hangisidir?",
                "{name}'{_suffix1} takımı hangisidir?",
                "{name}'{_suffix1} güncel takımı hangisidir?",
                "{name}'{_suffix1} şu an oynadığı takım hangisidir?"
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
                "{name}'{_suffix1} oynadığı lig hangisidir?",
                "{name}'{_suffix1} ligi hangisidir?",
                "{name}'{_suffix1} güncel ligi hangisidir?",
                "{name}'{_suffix1} şu an oynadığı takım hangisidir?"
            ]
        },
        "Bilim adamı": {
            "milliyeti": [
                "{name} nerelidir?",
                "{name} hangi ülke asıllıdır?",
                "{name} hangi millettendir?",
                "{name}'{_suffix1} hangi millettendir?"
            ],
            "çalıştığıyerler": [
                "{name}'{_suffix1} çalıştığı yerler nedir?",
                "{name}'{_suffix1} çalıştığı yerler nerelerdir?",
                "{name} nerelerde çalışmıştır?",
                "{name} nerelerde çalıştı?",
                "{name} nerelerde çalışmıştı?",
                "{name}'{_suffix1} çalıştığı kurumlar nerelerdir?",
                "{name} hangi kurumlarda çalışmıştır?",
                "{name}'{_suffix1} çalıştığı kurumlar nedir?",
            ],
            "ödüller": [
                "{name} hangi ödüllere sahiptir?",
                "{name} hangi ödülleri almıştır?",
                "{name} sahip olduğu ödüller nelerdir?",
                "{name}'{_suffix2} takdim edilen ödüller nelerdir?",
                "{name}'{_suffix2} verilen ödüller nelerdir?",
                "{name}'{_suffix1} kazandığı ödüller nelerdir?",
                "{name}'{_suffix1} sahip olduğu ödüller nelerdir?"
            ],
            "önemlibaşarıları": [
                "{name}'{_suffix1} önemli başarıları nelerdir?",
                "{name}'{_suffix1} sahip olduğu önemli başarılar nelerdir?",
                "{name}'{_suffix1} elde ettiği önemli başarılar nelerdir?",
                "{name}'{_suffix1} en önemli başarıları nelerdir?",
                "{name} en önemli başarıları nelerdir?"
            ],
            "vatandaşlığı": [
                "{name} hangi ülke vatandaşıdır?",
                "{name} hangi ülkenin vatandaşıdır?",
                "{name} nerenin vatandaşıdır?",
                "{name} vatandaşlığı hangi ülkedendir?",
                "{name}'{_suffix1} vatandaşlığı hangi ülkedendir?",
                "{name}'{_suffix1} vatandaşı olduğu ülke hangisidir?",
                "{name}'{_suffix1} vatandaşı olduğu ülke nedir?",
                "{name}'{_suffix1} vatandaşlığına sahip olduğu ülke nedir?",
                "{name}'{_suffix1} vatandaşlığına sahip olduğu ülke hangisidir?"
            ]
        },
        "Buz patencisi": {
            "ülke": [
                "{name} hangi ülke vatandaşıdır?",
                "{name} hangi ülke adına mücadele etmektedir?",
                "{name} hangi ülkenin sporcusudur?",
                "{name} hangi ülkenin sporcusuydu?",
                "{name} hangi ülkenin vatandaşıdır?",
                "{name} nerenin vatandaşıdır?",
                "{name} vatandaşlığı hangi ülkedendir?",
                "{name}'{_suffix1} vatandaşlığı hangi ülkedendir?",
                "{name}'{_suffix1} vatandaşı olduğu ülke hangisidir?",
                "{name}'{_suffix1} vatandaşı olduğu ülke nedir?",
                "{name}'{_suffix1} vatandaşlığına sahip olduğu ülke nedir?",
                "{name}'{_suffix1} vatandaşlığına sahip olduğu ülke hangisidir?"
            ],
            "koç": [
                "{name}'{_suffix1} koçu kimdir?",
                "{name}'{_suffix1} koçu kim?",
                "{name}'{_suffix1} koçu kimdi?",
                "{name}'{_suffix1} spor koçu kimdi?"
            ]
        },
        "Filozof": {
            "çağ": [
                "{name} hangi çağda yaşamaktaydı?",
                "{name} hangi çağda yaşadı?",
                "{name} yaşadığı çağ hangisiir?",
                "{name} hangi çağda yaşadı?",
                "{name} hangi çağda yaşadı?",
                "{name} hangi çağda yaşadı?"
            ],
            "bölge": [
                "{name} hangi bölgede yaşamaktaydı?",
                "{name} hangi bölgede yaşadı?"
            ],
            "etkilendikleri": [
                "{name} kimlerden etkilenmiştir?",
                "{name} kimlerden etkilendi?",
                "{name}'{_suffix1} etkilendiği kişiler kimlerdir?"
            ],
            "etkiledikleri": [
                "{name} kimleri etkilemiştir?",
                "{name} kimleri etkiledi?",
                "{name}'{_suffix1} etkilediği kişiler kimlerdir?"
            ],
            "ilgialanları": [
                "{name}'{_suffix1} ilgi alanları nelerdir?",
                "{name}'{_suffix1} ilgi alanları nelerdi?"
            ],
            "okulgelenek": [
                "{name}'{_suffix1} okulunun geleneği nedir?",
                "{name}'{_suffix1} okulunun gelenekleri nelerdir?"
            ]
        },
        "Hakem": {
            "turnuva": [
                "{name}'{_suffix1} görev aldığı turnuvalar hangileridir?",
                "{name} hangi turnuvalarda görev yapmıştır?",
                "{name} bulunduğu turnuvalar nelerdir?"
            ],
            "turnuva": [
                "{name}'{_suffix1} görevi nedir?",
                "{name} hangi görevi yapmaktadır?",
                "{name} üslendiği görev nedir?"
            ],
        },
        "Güreşçi": {
            "debut": [
                "{name}'{_suffix1} ilk ringe çıkışı ne zamandır?",
                "{name}'{_suffix1} ilk maça çıkışı ne zamandır?",
                "{name} ilk maçına ne zaman çıkmıştır?",
                "{name} ilk olarak ringe ne zaman çıkmıştır?"
            ],
            "ringadları": [
                "{name}'{_suffix1} ring adları nelerdir?",
                "{name}'{_suffix1} ring adları nedir?",
                "{name}'{_suffix1} ring adı nedir?"
            ],
            "eğiten": [
                "{name}'{_suffix1} eğiten kişiler kimlerdir?",
                "{name}'{_suffix1} eğiten kişilerin adları nelerdir?",
                "{name}'{_suffix1} eğiten kişilerin adları nedir?"
            ],
            "eğitildiğiyer": [
                "{name} nerede eğitilmiştir?",
                "{name} nerede eğitildi?",
                "{name} eğitildiği yer neresidir?",
                "{name} eğitildiği yer neresi"
            ],
            "yaşadığıyer": [
                "{name} nerede yaşamaktadır?",
                "{name} yaşadığı yer neresidir?",
                "{name} yaşadığı yer neresi"
            ],
            "emekliliği": [
                "{name} hangi yılda emekli olmuştur?",
                "{name} hangi yılda emekli olmuştu?"
            ]
        },
        "Futbolcu": {
            "pozisyon": [
                "{name} hangi pozisyonda oynamaktadır?",
                "{name} hangi pozisyonda oynar?",
                "{name} hangi pozisyonda oynuyor?",
                "{name} hangi mevkiide oynamaktadır?",
                "{name} hangi mevkiide oynar?",
                "{name} hangi mevkiide oynuyor?",
                "{name}'{_suffix1} oynadığı pozisyon nedir?",
                "{name}'{_suffix1} oynamakta olduğu pozisyon nedir?",
                "{name}'{_suffix1} pozisyonu nedir?",
                "{name}'{_suffix1} oyun pozisyonu nedir?",
                "{name}'{_suffix1} maçlardaki pozisyonu nedir?"
            ],
            "tamadı": [
                "{name}'{_suffix1} tam adı nedir?"
            ],
            "kulüp1": [
                "{name}'{_suffix1} ilk oynadığı takım hangisidir?",
                "{name}'{_suffix1} oynadığı ilk takım hangisidir?",
                "{name}'{_suffix1} ilk takımı hangisi?",
                "{name}'{_suffix1} ilk takımı hangisidir?",
                "{name}'{_suffix1} kariyerine başladığı takım hangisidir?",
                "{name}'{_suffix1} kariyerindeki ilk takım hangisidir?",
                "{name} profesyonel kariyerine hangi takımda başlamıştır?",
                "{name} profesyonel kariyerine hangi takımla başlamıştır?",
                "{name} profesyonel kariyerine hangi takımla adım atmıştır?",
                "{name}'{_suffix1} profesyonel kariyerindeki ilk takım hangisidir?",
                "{name}'{_suffix1} profesyonel kariyerindeki ilk takım hangisiydi?",
                "{name}'{_suffix1} profesyonel kariyerindeki ilk takım hangisi?",
                "{name}'{_suffix1} profesyonel kariyerindeki ilk takım nedir?",
                "{name}'{_suffix1} ilk oynadığı kulüp hangisidir?",
                "{name}'{_suffix1} oynadığı ilk kulüp hangisidir?",
                "{name}'{_suffix1} ilk kulübü hangisi?",
                "{name}'{_suffix1} ilk kulübü hangisidir?",
                "{name}'{_suffix1} kariyerine başladığı kulüp hangisidir?",
                "{name}'{_suffix1} kariyerindeki ilk kulüp hangisidir?",
                "{name} profesyonel kariyerine hangi kulüpte başlamıştır?",
                "{name} profesyonel kariyerine hangi kulüple başlamıştır?",
                "{name} profesyonel kariyerine hangi kulüple adım atmıştır?",
                "{name}'{_suffix1} profesyonel kariyerindeki ilk kulüp hangisidir?",
                "{name}'{_suffix1} profesyonel kariyerindeki ilk kulüp hangisiydi?",
                "{name}'{_suffix1} profesyonel kariyerindeki ilk kulüp hangisi?",
                "{name}'{_suffix1} profesyonel kariyerindeki ilk kulüp nedir?"
            ],
            "kulüpyıl1": [
                "{name} profesyonel kariyerine ne zaman başlamıştır?",
                "{name}'{_suffix1} profesyonel kariyerine başlangıcı ne zamandır?",
                "{name}'{_suffix1} profesyonel kariyerine başlangıcı ne zamandı",
                "{name}'{_suffix1} profesyonel kariyerine başlangıcı ne zaman",
                "{name}'{_suffix1} profesyonel kariyerine başlangıcı ne zaman oldu?",
                "{name}'{_suffix1} profesyonel kariyerine başlangıcı ne zaman olmuştur?",
                "{name} profesyonel kariyerine hangi yılda başladı?",
                "{name} profesyonel kariyerine hangi yılda başlamıştı?",
                "{name} profesyonel kariyerine hangi yılda başlamıştır?",
                "{name} profesyonel kariyerine ne zaman başladı?",
                "{name} profesyonel kariyerine ne zaman başlamıştı?",
                "{name} profesyonel kariyerine ne zaman başlamıştır?",
                "{name}'{_suffix1} ilk takımında ne zaman oynamıştır?",
                "{name}'{_suffix1} ilk takımında ne zamanlar oynamıştır?",
                "{name}'{_suffix1} ilk takımında hangi yıllar oynamıştır?",
                "{name}'{_suffix1} ilk takımında hangi yıllar oynadı?",
                "{name}'{_suffix1} ilk takımında oynadığı zaman aralığı nedir?",
                "{name}'{_suffix1} ilk takımında oynadığı zaman aralığı nedir?",
                "{name}'{_suffix1} ilk oynadığı takımda ne zaman oynamıştır?",
                "{name}'{_suffix1} ilk oynadığı takımda hangi yıllar arasında oynamıştır?",
                "{name}'{_suffix1} ilk oynadığı takımda hangi yıllar arasında oynamıştı?",
                "{name}'{_suffix1} ilk oynadığı takımda hangi yıllar arasında oynadı?"
            ],
            "kulüp2": [
                "{name}'{_suffix1} ikinci oynadığı takım hangisidir?",
                "{name}'{_suffix1} oynadığı ikinci takım hangisidir?",
                "{name}'{_suffix1} oynadığı ikinci takım nedir?",
                "{name}'{_suffix1} ikinci takımı nedir?",
                "{name}'{_suffix1} ikinci takımı hangisi?",
                "{name}'{_suffix1} ikinci takımı hangisidir?",
                "{name}'{_suffix1} kariyerindeki ikinci takım hangisidir?",
                "{name}'{_suffix1} kariyerindeki ikinci takım nedir?",
                "{name}'{_suffix1} profesyonel kariyerindeki ikinci takım hangisidir?",
                "{name}'{_suffix1} profesyonel kariyerindeki ikinci takım hangisiydi?",
                "{name}'{_suffix1} profesyonel kariyerindeki ikinci takım hangisi?",
                "{name}'{_suffix1} profesyonel kariyerindeki ikinci takım nedir?"
            ],
            "kulüpyıl2": [
                "{name}'{_suffix1} ikinci takımında ne zaman oynamıştır?",
                "{name}'{_suffix1} ikinci takımında ne zamanlar oynamıştır?",
                "{name} ikinci takımında hangi yıllar oynamıştır?",
                "{name} ikinci takımında hangi yıllar oynadı?",
                "{name}'{_suffix1} ikinci takımında oynadığı zaman aralığı nedir?",
                "{name} ikinci takımında oynadığı zaman aralığı nedir?",
                "{name}'{_suffix1} ikinci oynadığı takımda ne zaman oynamıştır?",
                "{name} ikinci oynadığı takımda ne zaman oynamıştır?",
                "{name}'{_suffix1} ikinci oynadığı takımda hangi yıllar arasında oynamıştır?",
                "{name}'{_suffix1} ikinci oynadığı takımda hangi yıllar arasında oynamıştı?",
                "{name}'{_suffix1} ikinci oynadığı takımda hangi yıllar arasında oynadı?",
                "{name}'{_suffix1} oynadığı ikinci takımda hangi yıllar arasında oynadı?",
                "{name}'{_suffix1} oynadığı ikinci takımda hangi yıllar arasında oynamıştır?",
                "{name}'{_suffix1} oynadığı ikinci takımda hangi yıllar arasında oynamıştı?",
                "{name}'{_suffix1} oynadığı ikinci takımda hangi periyotta oynamıştı?",
                "{name}'{_suffix1} oynadığı ikinci takımda hangi periyotta oynamıştır?"
            ]
        },
        "Kişi": {
            "meslek": [
                "{name}'{_suffix1} mesleği nedir?",
                "{name} ne iş yapar?",
                "{name} işi nedir?"
            ],
            "aktifyılları": [
                "{name} hangi yıllar arası aktifti?",
                "{name} hangi yıllar arası aktif kalmıştır?",
                "{name}'{_suffix1} aktif yılları nedir?"
            ],
            "yer": [
                "{name} nerede yaşamaktadır?",
                "{name} yaşadığı yer neresidir?",
                "{name} yaşadığı yer neresi"
            ],
            "etinyılları": [
                "{name} hangi yıllar arası etkindi?",
                "{name} hangi yıllar arası etkin kalmıştır?",
                "{name}'{_suffix1} etkin yılları nedir?"
            ],
        },
        "Kraliyet": {
            "hükümsüresi": [
                "{name} hangi yıllar arası hüküm sürmüştür?",
                "{name} hangi yıllar arası hüküm sürdü?",
                "{name} hangi yıllar arasında hüküm sürdü?",
                "{name} hangi yıllar arasında hüküm sürmüştür?"
            ],
            "sonragelen": [
                "{name}'{_suffix3} sonra gelen hükümdar kimir?",
                "{name}'{_suffix3} sonra hangi hükümdar gelmiştir?",
                "{name}'{_suffix3} sonra tahta kim geçmiştir?",
                "{name}'{_suffix1} ardından kim hüküm sürmüştür?",
                "{name}'{_suffix1} ardından kim tahta geçmiştir?"
            ],
            "öncegelen": [
                "{name}'{_suffix3} önce gelen hükümdar kimdir?",
                "{name}'{_suffix3} önce kim hüküm sürmekteydi?",
                "{name} kimin ardından tahta çıkmıştır?",
                "{name} hangi hükümdardan sonra gelmiştir?",
                "{name} hangi tahtı kimden devralmıştır?"
            ],
            "babası": [
                "{name}'{_suffix1} babası kimdir?",
                "{name}'{_suffix1} babasının adı nedir?"
            ],
            "hanedan": [
                "{name}'{_suffix1} hanedanı nedir?",
                "{name} hangi hanedandandır?"
            ],
            "annesi": [
                "{name}'{_suffix1} annesi kimdir?",
                "{name}'{_suffix1} annesinin adı nedir?"
            ],
        },
        "Makam sahibi": {
            "makam": [
                "{name} hangi makama sahiptir?",
                "{name} hangi makamdadır?",
                "{name} hangi makamda görev almıştır?",
                "{name}'{_suffix1} görevi nedir"
            ],
            "dönembaşı": [
                "{name} göreve ne zaman başlamıştır?",
                "{name} ilk görev yılı nedir?",
                "{name} göreve ne zaman gelmiştir?",
                "{name} dönemi ne zaman başlamıştır?"
            ],
            "öncegelen": [
                "{name}'{_suffix3} önce gelen kişi kimdir?",
                "{name}'{_suffix3} önce gelen kişi kim?",
                "{name}'{_suffix3} önce görev alan kişi kim?",
                "{name}'{_suffix3} önce görev alan kişi kimdir?"
            ],
            "dönemsonu": [
                "{name} en son hangi yıl görev yapmıştır?",
                "{name} görevini ne zaman devretmiştir?",
                "{name}'{_suffix1} son görev yılı ne zamandır?",
                "{name}'{_suffix1} görevi ne zaman sona ermiştir?"
            ],
            "sonragelen": [
                "{name}'{_suffix3} sonra gelen kişi kimdir?",
                "{name}'{_suffix3} sonra gelen kişi kim?",
                "{name}'{_suffix3} sonra görev alan kişi kim?",
                "{name}'{_suffix3} sonra görev alan kişi kimdir?"
            ],
            "partisi": [
                "{name} hangi partinin mensubudur?",
                "{name}'{_suffix1} partisi nedir?",
            ]
        },
        "Manken": {
            "gözrengi": [
                "{name}'{_suffix1} göz rengi nedir?",
                "{name}'{_suffix1} gözü hangi renktir"
            ],
            "saçrengi": [
                "{name}'{_suffix1} saç rengi nedir?",
                "{name}'{_suffix1} saçı hangi renktir?"
            ],
            "ulus": [
                "{name} nerelidir?",
                "{name} hangi ülke asıllıdır?",
                "{name} hangi millettendir?",
                "{name}'{_suffix1} uyruğu neresidir"
            ],
            "boy": [
                "{name}'{_suffix1} boyu ne kadardır?",
                "{name}'{_suffix1} boyu nedir?",
            ]
        },
        "Müzik sanatçısı": {
            "artalan": [
                "{name}'{_suffix1} art alanı nedir?",
                "{name} hangi türden gelmektedir"
            ],
            "tarz": [
                "{name} hangi tür müzik yapar?",
                "{name}'{_suffix1} hangi tarzda müzik yapmaktadır?",
                "{name}'{_suffix1} hangi tarzda müzik yapmakta",
                "{name}'{_suffix1} hangi tarzda müzik yapar?",
                "{name}'{_suffix1} hangi tarzlarda müzik yapmaktadır?",
                "{name}'{_suffix1} müzik tarzı nedir",
                "{name}'{_suffix1} tarzı nedir",
                "{name}'{_suffix1} ne tarz müzik yapmaktadır?",
                "{name}'{_suffix1} ne tarzda müzik yapar?",
                "{name}'{_suffix1} hangi tarzda müzik yapmaktadır?",
                "{name}'{_suffix1} ne tarzda müzik yapmaktadır?",
            ],
            "etkinyıllar": [
                "{name} hangi yıllarda aktif olarak müzik yapmıştır?",
                "{name} hangi yıllarda müzisyenlik yapmıştı?",
                "{name} aktif yılları nelerdir?"
                "{name} aktif yılları nedir?"
                "{name} etkin yılları nelerdir?"
                "{name} etkin yılları nedir?"
                "{name} etkin olduğu yıllar nedir?"
            ],
            "meslek": [
                "{name}'{_suffix1} gerçek mesleği",
                "{name}'{_suffix1} gerçek mesleği nedir?",
                "{name}'{_suffix1} mesleği nedir?",
                "{name} mesleği nedir?",
                "{name} hangi mesleğe mensuptur?",
                "{name} hangi mesleği yapıyordu?",
                "{name} hangi işi yapıyor?",
                "{name} hangi işi yapıyordu?"
            ],
            "plakşirketi": [
                "{name} hangi plak şirketiyle çalışmaktadır?",
                "{name} hangi plak şirketiyle çalışıyordu?",
                "{name} hangi plak şirketiyle çalışıyor?",
            ],
            "köken": [
                "{name} nerelidir?",
                "{name} hangi ülke asıllıdır?",
                "{name} hangi millettendir?",
                "{name}'{_suffix1} hangi millettendir?",
                "{name} kökeni nedir?",
            ],
            "çalgı": [
                "{name} hangi çalgıyı çalmaktadır?",
                "{name} hangi çalgıyı çalar?",
                "{name} hangi çalgıyı çalıyor?",
                "{name} hangi müzik aletini çalmaktadır?",
                "{name} hangi müzik aletini çalar?",
                "{name} hangi müzik aletini çalıyor?"
            ]
        },
        "Oyuncu": {
            "yer": [
                "{name} nerede yaşamaktadır?",
                "{name} yaşadığı yer neresidir?",
                "{name} ikamet ettiği yer neresidir?"
            ],
            "meslek": [
                "{name}'{_suffix1} gerçek mesleği nedir?",
                "{name}'{_suffix1} mesleği nedir?",
                "{name} mesleği nedir?",
                "{name} hangi mesleğe mensuptur?",
                "{name} hangi işi yapıyor?",
            ],
            "etkinyıllar": [
                "{name} hangi yıllarda aktif olarak rol almıştır?",
                "{name} aktif yılları nelerdir?"
                "{name} aktif yılları nedir?"
                "{name} etkin yılları nelerdir?"
                "{name} etkin yılları nedir?"
                "{name} etkin olduğu yıllar nedir?"
            ],
            "evlilik": [
                "{name} eşi kimdir?"
                "{name}'{_suffix1} eşi kimdir?",
                "{name} kiminle evlidir?",
                "{name} kiminle evlendi?"
            ],
            "ulus": [
                "{name} nerelidir?",
                "{name} hangi ülke asıllıdır?",
                "{name} hangi millettendir?",
                "{name}'{_suffix1} hangi millettendir?"
            ]
        },
        "Profesyonel güreşçi": {
            "debut": [
                "{name}'{_suffix1} ilk ringe çıkışı ne zamandır?",
                "{name}'{_suffix1} ilk maça çıkışı ne zamandır?",
                "{name} ilk maçına ne zaman çıkmıştır?",
                "{name} ilk olarak ringe ne zaman çıkmıştır?"
            ],
            "ringadları": [
                "{name}'{_suffix1} ring adları nelerdir?",
                "{name}'{_suffix1} ring adları nedir?",
                "{name}'{_suffix1} ring adı nedir?"
            ],
            "eğiten": [
                "{name}'{_suffix1} eğiten kişiler kimlerdir?",
                "{name}'{_suffix1} eğiten kişilerin adları nelerdir?",
            ],
            "eş": [
                "{name} kimle evlidir?",
                "{name}'{_suffix1} evli olduğu kişi kimdir?",
            ],
            "eğitildiğiyer": [
                "{name} nerede eğitilmiştir?",
                "{name} nerede eğitildi?",
                "{name} eğitildiği yer neresidir?",
                "{name} eğitildiği yer neresi"
            ],
            "çocuklar": [
                "{name}'{_suffix1} çocukları kimlerdir?",
                "{name}'{_suffix1} çocukları kim?",
                "{name}'{_suffix1} çocuklarının adları nedir?",
                "{name}'{_suffix1} çocuklarının adları nelerdir?",
                "{name} çocukları kimdir?",
                "{name} çocuklarının isimleri nedir?",
                "{name} çocuklarının isimleri?"
            ]
        },
        "Sanatçı": {
            "alanı": [
                "{name}'{_suffix1} alanı nedir?",
                "{name} hangi alanda sanat yapmaktadır?",
                "{name} hangi alanda sanat yapmaktaydı?",
                "{name} hangi alanda sanat yapıyor?",
                "{name} hangi alanda eser vermektedir"
            ],
            "milliyeti": [
                "{name} nerelidir?",
                "{name} hangi ülke asıllıdır?",
                "{name} hangi millettendir?",
                "{name}'{_suffix1} hangi millettendir?"
            ],
            "yer": [
                "{name} nerede yaşamaktadır?",
                "{name} yaşadığı yer neresidir?",
                "{name} yaşadığı yer neresi"
            ],
            "ünlüyapıtları": [
                "{name}'{_suffix1} ünlü yapıtları nelerdir?",
                "{name}'{_suffix1} ünlü yapıtları nedir?",
                "{name}'{_suffix1} yarattığı ünlü yapıtlar nelerdir?",
                "{name}'{_suffix1} yarattığı ünlü yapıtlar nedir?",
            ]
        },
        "Sporcu": {
            "ülke": [
                "{name} hangi ülke adına ter dökmektedir?",
                "{name} hangi ülkenin sporcusudur?",
                "{name} hangi ülke adına yarışmaktadır?",
            ],
            "spor": [
                "{name} hangi spor dalındadır?",
                "{name} hangi spor dalında mücadele etmektedir?",
                "{name} hangi sporu yapmaktadır?"
            ],
            "uyruk": [
                "{name} nerelidir?",
                "{name} hangi ülke asıllıdır?",
                "{name} hangi millettendir?",
                "{name}'{_suffix1} hangi millettendir?"
            ],
            "kei": [
                "{name}'{_suffix1} en iyi derecesi nedir?",
                "{name}'{_suffix1} kariyerinde elde ettiği en yüksek derece nedir?",
                "{name}'{_suffix1} elde ettiği en yüksek başarı nedir?"
            ],
            "ağırlık": [
                "{name}'{_suffix1} kilosu nedir?",
                "Ünlü sporcu {name} kaç kilodur?",
                "{name}'{_suffix1} ağırlığı nedir?",
            ]
        },
        "Tenis sporcu": {
            "vatandaşlık": [
                "{name} hangi ülke vatandaşıdır?",
                "{name} hangi ülkenin vatandaşıdır?",
                "{name} nerenin vatandaşıdır?",
                "{name}'{_suffix1} vatandaşlığı hangi ülkedendir?",
                "{name}'{_suffix1} vatandaşı olduğu ülke hangisidir?",
                "{name}'{_suffix1} vatandaşı olduğu ülke nedir?",
                "{name}'{_suffix1} vatandaşlığına sahip olduğu ülke nedir?",
                "{name}'{_suffix1} vatandaşlığına sahip olduğu ülke hangisidir?"
            ],
            "enyükseksıralama": [
                "{name}'{_suffix1} en iyi derecesi nedir?",
                "{name}'{_suffix1} en yüksek sıralaması nedir?",
                "{name}'{_suffix1} kariyerinde elde ettiği en yüksek sıralama nedir?",
                "{name}'{_suffix1} elde ettiği en yüksek başarı nedir?"
            ],
            "oyunstili": [
                "{name}'{_suffix1} oyun stili nedir?",
                "{name} hangi stilde oynamaktadır?"
            ],
            "wimbledonsonuçları": [
                "{name}'{_suffix1} Wimbledon sonuçları nedir?",
                "{name} Wimbledon'da hangi sonucu elde etmiştir?",
                "{name} Wimbledon sonuçları nasıldır?"
            ],
            "amerikaaçıksonuçları": [
                "{name}'{_suffix1} Amerika açık sonuçları nedir?",
                "{name} Amerika açıkta hangi sonucu elde etmiştir?",
                "{name} Amerika açık sonuçları nasıldır?"
            ],
            "fransaaçıksonuçları": [
                "{name}'{_suffix1} Fransa açık sonuçları nedir?",
                "{name} Fransa açıkta hangi sonucu elde etmiştir?",
                "{name} Fransa açık sonuçları nasıldır?"

            ],
            "avustralyaaçıksonuçları": [
                "{name}'{_suffix1} Avustralya açık sonuçları nedir?",
                "{name} Avustralya açıkta hangi sonucu elde etmiştir?",
                "{name} Avustralya açık sonuçları nasıldır?"
            ],
            "toplamkupa": [
                "{name}'{_suffix1} kazandığı toplam kupa sayısı kaçtır?",
                "{name} kariyerinde toplam kaç tane kupa kazanmıştır?",
                "{name} toplam kaç adet kupa kazanmıştır?",
                "{name} kaç adet kupaya sahiptir?",
                "{name}'{_suffix1} sahip olduğu kupa sayısı nedir?"

            ],
            "yaşadığıyer": [
                "{name} nerede yaşamaktadır?",
                "{name} yaşadığı yer neresidir?"
            ]
        },
        "Voleybolcu": {
            "pozisyon": [
                "{name} hangi pozisyonda oynamaktadır?",
                "{name} hangi pozisyonda oynar?",
                "{name} hangi pozisyonda oynuyor?",
                "{name} hangi mevkiide oynamaktadır?",
                "{name} hangi mevkiide oynar?",
                "{name} hangi mevkiide oynuyor?",
                "{name}'{_suffix1} oynadığı pozisyon nedir?",
                "{name}'{_suffix1} oynamakta olduğu pozisyon nedir?",
                "{name}'{_suffix1} pozisyonu nedir?",
                "{name}'{_suffix1} oyun pozisyonu nedir?",
                "{name}'{_suffix1} maçlardaki pozisyonu nedir?"
            ],
            "milliyeti": [
                "{name} nerelidir?",
                "{name} hangi ülke asıllıdır?",
                "{name} hangi millettendir?",
                "{name}'{_suffix1} uyruğu nedir?"
            ],
            "kulüptakım": [
                "{name} hangi takımlarda oynamıştır?",
                "{name} geçmişte hangi takımlarda oynamıştır?",
                "{name} daha önce oynadığı takımlar nelerdir?",
                "{name} bulunduğu takımlar hangileridir?",

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
                "{name}'{_suffix1} oynadığı takım hangisidir?",
                "{name}'{_suffix1} takımı hangisidir?",
                "{name}'{_suffix1} güncel takımı hangisidir?",
                "{name}'{_suffix1} şu an oynadığı takım hangisidir?"
            ],
            "numarası": [
                "{name}'{_suffix1} forma numarası nedir?",
                "{name}'{_suffix1} forması kaç numaradır?",
                "{name}'{_suffix1} forması kaç numaraydı?",
                "{name} kaç numaralı formayı giymektedir?",
                "{name} kaç numaralı formayı giymişti?",
                "{name} hangi forma numarasına sahiptir?",
                "{name}'{_suffix1} sahip olduğu forma numarası nedir?"
            ],
            "millitakım": [
                "{name} hangi milli takımda oynamaktadır?",
                "{name} hangi milli takımda oynuyor?",
                "{name} hangi milli takımda oynamakta?",
                "{name} hangi ülkenin milli takımında oynamaktadır?",
                "{name} hangi ülkenin milli takımında oynadı?",
                "{name} oynadığı milli takım hangisidir?",
                "{name}'{_suffix1} oynadığı milli takım hangisidir?",
                "{name}'{_suffix1} oynadığı milli takım hangisi?",
                "{name}'{_suffix1} oynadığı milli takım nedir?",
                "{name} nerenin milli takımında oynamaktadır?",
                "{name} nerenin milli takımında oynamıştı?",
                "{name} nerenin milli takımında oynuyor?",
                "{name} nerenin milli takımında oynadı?"
            ],
        },
        "Yazar": {
            "meslek": [
                "{name}'{_suffix1} gerçek mesleği nedir?",
                "{name}'{_suffix1} mesleği nedir?",
                "{name} mesleği nedir?",
                "{name} hangi mesleğe mensuptur?",
                "{name} hangi mesleği yapıyordu?",
                "{name} hangi işi yapıyor?",
                "{name} hangi işi yapıyordu?"
            ],
            "tür": [
                "{name} hangi türde eser vermiştir?",
                "{name} hangi türde eserler vermiştir?",
                "{name} hangi türde yazmıştır?",
                "{name} hangi türde yazmaktaydır?",
                "{name}'{_suffix1} eserleri hangi türdedir?",
                "{name}'{_suffix1} eser türleri?",
                "{name}'{_suffix1} eserleri hangi türdedir?",
                "{name}'{_suffix1} eserleri hangi türdeydi?",
                "{name}'{_suffix1} eser türü nedir?"
            ],
            "dönem": [
                "{name} hangi dönemde eser vermiştir?",
                "{name} hangi dönemde eserler vermiştir?",
                "{name} hangi dönem yazarıdır?",
                "{name} eser verdiği dönem nedir?",
                "{name} eser verdiği dönem hangisidir?"
            ],
            "ilkeser": [
                "{name}'{_suffix1} ilk eseri nedir?",
                "{name}'{_suffix1} ilk eseri hangisidir?",
                "{name}'{_suffix1} ilk eserinin adı nedir?",
                "{name}'{_suffix1} verdiği ilk eserinin adı nedir?",
                "{name}'{_suffix1} verdiği ilk eseri nedir?",
                "{name}'{_suffix1} verdiği ilk eseri hangisidir?"
                "Yazar {name}'{_suffix1} ilk eseri nedir?"
            ]
        }
    }
