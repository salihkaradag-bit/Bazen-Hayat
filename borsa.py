import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import seaborn as sns
from datetime import datetime, timedelta
from tabulate import tabulate
from colorama import Fore, Back, Style, init
import warnings

warnings.filterwarnings('ignore')

# Colorama'yı başlat
init(autoreset=True)

# Grafik stilini ayarla
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# BIST 100 hisseleri (en popüler olanlar)
BIST_100_STOCKS = [
    'AEFES', 'AGHOL', 'AGROT', 'AHGAZ', 'AKBNK', 'AKSA', 'AKSEN', 'ALARK', 'ALFAS', 'ALTNY',
    'ANHYT', 'ANSGR', 'ARCLK', 'ARDYZ', 'ASELS', 'ASTOR', 'AVPGY', 'BERA', 'BIMAS', 'BRSAN',
    'BRYAT', 'BSOKE', 'BTCIM', 'CANTE', 'CCOLA', 'CIMSA', 'CLEBI', 'CWENE', 'DOAS', 'DOHOL',
    'ECILC', 'EFOR', 'EGEEN', 'EKGYO', 'ENERY', 'ENJSA', 'ENKAI', 'EREGL', 'EUPWR', 'FROTO',
    'GARAN', 'GESAN', 'GOLTS', 'GRTHO', 'GSRAY', 'GUBRF', 'HALKB', 'HEKTS', 'IEYHO', 'ISCTR',
    'ISMEN', 'KARSN', 'KCAER', 'KCHOL', 'KONTR', 'KONYA', 'KRDMD', 'KTLEV', 'LMKDC', 'MAGEN',
    'MAVI', 'MGROS', 'MIATK', 'MPARK', 'OBAMS', 'ODAS', 'OTKAR', 'OYAKC', 'PASEU', 'PETKM',
    'PGSUS', 'RALYH', 'REEDR', 'RYGYO', 'SAHOL', 'SASA', 'SELEC', 'SISE', 'SKBNK', 'SMRTG',
    'SOKM', 'TABGD', 'TAVHL', 'TCELL', 'THYAO', 'TKFEN', 'TOASO', 'TRALT', 'TRENJ', 'TRMET',
    'TSKB', 'TTKOM', 'TTRAK', 'TUPRS', 'TURSG', 'ULKER', 'VAKBN', 'VESTL', 'YEOTK', 'YKBNK',
    'ZOREN'
]

# Listenin doğruluğunu kontrol etmek için:
print(f"Listede toplam {len(BIST_100_STOCKS)} adet hisse senedi var.")


def detect_asset_type(symbol):
    """
    Sembolün hisse mi yoksa fon mu olduğunu tespit eder
    """
    symbol = symbol.upper().strip()

    # BIST 100 listesi kontrolü
    if symbol == '100':
        return "BIST100"

    # Fon kodları genellikle şu formatlarda olur:
    # AFA, TTE, İJH gibi 3 harfli kodlar
    # veya TURKSS, AZNVD gibi özel kodlar

    # BIST hisseleri genellikle 4-5 harfli ve .IS ile biter
    if len(symbol) <= 4 and not any(c.isdigit() for c in symbol):
        # Kısa kodlar genellikle fon olabilir
        return "FON"
    elif symbol.endswith('.IS'):
        return "HISSE"
    else:
        # Varsayılan olarak hisse dene, olmazsa fon dene
        return "UNKNOWN"


def format_fund_symbol(symbol):
    """
    Fon sembolünü yfinance için uygun format
    """
    # Fonlar için doğrudan kodu kullan
    return symbol.upper()


def format_stock_symbol(symbol):
    """
    Hisse senedi sembolünü yfinance için uygun format
    """
    symbol = symbol.upper()
    if not symbol.endswith('.IS') and symbol != '100':
        symbol = symbol + '.IS'
    return symbol


def get_bist100_list():
    """
    BIST 100 hisselerini ve günlük değişimlerini listeler
    """
    print(f"\n{Fore.CYAN}{'=' * 80}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}📊 BIST 100 Hisseleri ve Günlük Değişimleri{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'=' * 80}{Style.RESET_ALL}")

    results = []
    total_changes = []

    print(f"{Fore.GREEN}Veriler alınıyor... (Bu işlem 30-60 saniye sürebilir){Style.RESET_ALL}")

    for i, symbol in enumerate(BIST_100_STOCKS, 1):
        try:
            stock_symbol = format_stock_symbol(symbol)
            stock = yf.Ticker(stock_symbol)

            # Günlük değişim için veri
            hist = stock.history(period="2d")

            if not hist.empty and len(hist) >= 2:
                current_price = hist['Close'].iloc[-1]
                prev_close = hist['Close'].iloc[-2]

                daily_change = current_price - prev_close
                daily_change_percent = (daily_change / prev_close) * 100

                # İlerleme göstergesi
                progress = f"%{int(i / len(BIST_100_STOCKS) * 100)}"
                print(f"{Fore.CYAN}{progress} İşleniyor: {symbol}{Style.RESET_ALL}", end='\r')

                # Şirket ismini al
                info = stock.info
                company_name = info.get('longName', symbol)[:30]  # İlk 30 karakter

                results.append({
                    'No': i,
                    'Sembol': symbol,
                    'Şirket': company_name,
                    'Fiyat': current_price,
                    'Değişim ₺': daily_change,
                    'Değişim %': daily_change_percent
                })

                total_changes.append(daily_change_percent)
            else:
                results.append({
                    'No': i,
                    'Sembol': symbol,
                    'Şirket': 'Veri yok',
                    'Fiyat': 0,
                    'Değişim ₺': 0,
                    'Değişim %': 0
                })

        except Exception as e:
            results.append({
                'No': i,
                'Sembol': symbol,
                'Şirket': f'Hata: {str(e)[:20]}',
                'Fiyat': 0,
                'Değişim ₺': 0,
                'Değişim %': 0
            })

    print(f"\n{Fore.GREEN}Veriler hazırlanıyor...{Style.RESET_ALL}")

    # DataFrame oluştur
    df = pd.DataFrame(results)

    # Sıralama seçeneği sor
    print(f"\n{Fore.YELLOW}Nasıl sıralamak istersiniz?{Style.RESET_ALL}")
    print("1 - Sembole göre (A-Z)")
    print("2 - Değişime göre (En çok artan)")
    print("3 - Değişime göre (En çok azalan)")
    print("4 - Fiyata göre (En yüksek)")
    print("5 - Fiyata göre (En düşük)")
    print("6 - Varsayılan (Liste sırası)")

    sort_choice = input(f"{Fore.GREEN}Seçiminiz (1-6, varsayılan=6): {Style.RESET_ALL}").strip()

    if sort_choice == '1':
        df = df.sort_values('Sembol')
    elif sort_choice == '2':
        df = df.sort_values('Değişim %', ascending=False)
    elif sort_choice == '3':
        df = df.sort_values('Değişim %', ascending=True)
    elif sort_choice == '4':
        df = df.sort_values('Fiyat', ascending=False)
    elif sort_choice == '5':
        df = df.sort_values('Fiyat', ascending=True)

    # Tabloyu göster
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 30)

    # Renkli tablo için formatla
    def color_change(val):
        if val > 0:
            return f'{Fore.GREEN}▲ {val:+.2f}%{Style.RESET_ALL}'
        elif val < 0:
            return f'{Fore.RED}▼ {val:+.2f}%{Style.RESET_ALL}'
        else:
            return f'{Fore.YELLOW}● {val:.2f}%{Style.RESET_ALL}'

    def color_price_change(val):
        if val > 0:
            return f'{Fore.GREEN}+{val:.2f}{Style.RESET_ALL}'
        elif val < 0:
            return f'{Fore.RED}{val:.2f}{Style.RESET_ALL}'
        else:
            return f'{Fore.YELLOW}{val:.2f}{Style.RESET_ALL}'

    # Tabloyu yazdır
    print(f"\n{Fore.CYAN}{'=' * 100}{Style.RESET_ALL}")

    for idx, row in df.iterrows():
        change_color = Fore.GREEN if row['Değişim %'] > 0 else Fore.RED if row['Değişim %'] < 0 else Fore.YELLOW
        arrow = "▲" if row['Değişim %'] > 0 else "▼" if row['Değişim %'] < 0 else "●"

        print(f"{Fore.CYAN}{int(row['No']):3d}{Style.RESET_ALL} | "
              f"{Fore.YELLOW}{row['Sembol']:6s}{Style.RESET_ALL} | "
              f"{row['Şirket']:30s} | "
              f"{Fore.WHITE}{row['Fiyat']:8.2f} ₺{Style.RESET_ALL} | "
              f"{change_color}{arrow} {row['Değişim ₺']:+.2f} ₺{Style.RESET_ALL} | "
              f"{change_color}{row['Değişim %']:+.2f}%{Style.RESET_ALL}")

    print(f"{Fore.CYAN}{'=' * 100}{Style.RESET_ALL}")

    # Özet istatistikler
    if total_changes:
        avg_change = sum(total_changes) / len([x for x in total_changes if x != 0])
        positive_count = len([x for x in total_changes if x > 0])
        negative_count = len([x for x in total_changes if x < 0])
        neutral_count = len([x for x in total_changes if x == 0])

        print(f"\n{Fore.YELLOW}📊 BIST 100 ÖZETİ{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Ortalama Değişim: {avg_change:+.2f}%{Style.RESET_ALL}")
        print(f"{Fore.GREEN}📈 Yükselen: {positive_count}{Style.RESET_ALL}")
        print(f"{Fore.RED}📉 Düşen: {negative_count}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}⚖️  Değişmeyen: {neutral_count}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Toplam: {len(total_changes)}{Style.RESET_ALL}")

    print(f"\n{Fore.GREEN}Detaylı inceleme için hisse sembolünü girebilirsiniz.{Style.RESET_ALL}")


def get_fund_info(symbol):
    """
    Fon bilgilerini getir
    """
    try:
        # Fon sembolünü düzenle
        fund_symbol = format_fund_symbol(symbol)

        # Fon verilerini çek
        fund = yf.Ticker(fund_symbol)

        # Fon bilgileri
        info = fund.info

        # Farklı periyotlar için veriler
        hist_1m = fund.history(period="1mo")
        hist_3m = fund.history(period="3mo")
        hist_6m = fund.history(period="6mo")
        hist_1y = fund.history(period="1y")

        if hist_1m.empty:
            # Alternatif olarak hisse formatını dene
            stock_symbol = format_stock_symbol(symbol)
            stock = yf.Ticker(stock_symbol)
            hist_1m = stock.history(period="1mo")
            hist_3m = stock.history(period="3mo")
            hist_6m = stock.history(period="6mo")
            hist_1y = stock.history(period="1y")

            if hist_1m.empty:
                print(f"{Fore.RED}Fon verisi bulunamadı: {symbol}")
                return None
            else:
                print(f"{Fore.YELLOW}Hisse senedi olarak bulundu: {stock_symbol}")

        # Mevcut fiyat
        current_price = hist_1m['Close'].iloc[-1] if not hist_1m.empty else 0
        prev_close = hist_1m['Close'].iloc[-2] if len(hist_1m) > 1 else current_price

        # Değişim hesaplamaları
        daily_change = current_price - prev_close
        daily_change_percent = (daily_change / prev_close) * 100 if prev_close else 0

        # Haftalık değişim
        weekly_data = hist_1m.last('5d')
        week_start_price = weekly_data['Close'].iloc[0] if len(weekly_data) > 0 else current_price
        weekly_change = current_price - week_start_price
        weekly_change_percent = (weekly_change / week_start_price) * 100 if week_start_price else 0

        # Aylık değişim
        month_start_price = hist_1m['Close'].iloc[0] if not hist_1m.empty else current_price
        monthly_change = current_price - month_start_price
        monthly_change_percent = (monthly_change / month_start_price) * 100 if month_start_price else 0

        # 3 aylık değişim
        three_month_start = hist_3m['Close'].iloc[0] if not hist_3m.empty else current_price
        three_month_change = current_price - three_month_start
        three_month_change_percent = (three_month_change / three_month_start) * 100 if three_month_start else 0

        # 6 aylık değişim
        six_month_start = hist_6m['Close'].iloc[0] if not hist_6m.empty else current_price
        six_month_change = current_price - six_month_start
        six_month_change_percent = (six_month_change / six_month_start) * 100 if six_month_start else 0

        # Son 1 aylık en düşük/en yüksek
        month_low = hist_1m['Low'].min() if not hist_1m.empty else 0
        month_high = hist_1m['High'].max() if not hist_1m.empty else 0

        # Son 1 yıllık en düşük/en yüksek
        year_low = hist_1y['Low'].min() if not hist_1y.empty else 0
        year_high = hist_1y['High'].max() if not hist_1y.empty else 0

        # Fon ismi
        fund_name = info.get('longName', info.get('shortName', symbol))

        # Fon tipi
        fund_type = info.get('fundFamily', 'Bilinmiyor')

        return {
            'type': 'FON',
            'symbol': symbol,
            'name': fund_name,
            'fund_type': fund_type,
            'current_price': current_price,
            'daily': (daily_change, daily_change_percent),
            'weekly': (weekly_change, weekly_change_percent),
            'monthly': (monthly_change, monthly_change_percent),
            'three_month': (three_month_change, three_month_change_percent),
            'six_month': (six_month_change, six_month_change_percent),
            'month_low': month_low,
            'month_high': month_high,
            'year_low': year_low,
            'year_high': year_high,
            'hist_1m': hist_1m,
            'hist_3m': hist_3m,
            'hist_6m': hist_6m,
            'hist_1y': hist_1y,
            'last_update': datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        }

    except Exception as e:
        print(f"{Fore.RED}Fon bilgisi alınırken hata: {str(e)}")
        return None


def get_stock_info(symbol):
    """
    Hisse senedi bilgilerini getir
    """
    try:
        stock_symbol = format_stock_symbol(symbol)
        stock = yf.Ticker(stock_symbol)

        info = stock.info

        # Farklı periyotlar için veriler
        hist_1d = stock.history(period="1d", interval="1m")
        hist_1w = stock.history(period="5d")
        hist_1m = stock.history(period="1mo")
        hist_3m = stock.history(period="3mo")
        hist_6m = stock.history(period="6mo")
        hist_1y = stock.history(period="1y")

        if hist_1m.empty:
            print(f"{Fore.RED}Hisse verisi bulunamadı: {stock_symbol}")
            return None

        current_price = hist_1m['Close'].iloc[-1] if not hist_1m.empty else 0
        prev_close = info.get('previousClose', hist_1m['Close'].iloc[-2] if len(hist_1m) > 1 else current_price)

        # Değişim hesaplamaları
        daily_change = current_price - prev_close
        daily_change_percent = (daily_change / prev_close) * 100 if prev_close else 0

        week_start_price = hist_1w['Close'].iloc[0] if not hist_1w.empty else current_price
        weekly_change = current_price - week_start_price
        weekly_change_percent = (weekly_change / week_start_price) * 100 if week_start_price else 0

        month_start_price = hist_1m['Close'].iloc[0] if not hist_1m.empty else current_price
        monthly_change = current_price - month_start_price
        monthly_change_percent = (monthly_change / month_start_price) * 100 if month_start_price else 0

        three_month_start = hist_3m['Close'].iloc[0] if not hist_3m.empty else current_price
        three_month_change = current_price - three_month_start
        three_month_change_percent = (three_month_change / three_month_start) * 100 if three_month_start else 0

        six_month_start = hist_6m['Close'].iloc[0] if not hist_6m.empty else current_price
        six_month_change = current_price - six_month_start
        six_month_change_percent = (six_month_change / six_month_start) * 100 if six_month_start else 0

        month_low = hist_1m['Low'].min() if not hist_1m.empty else 0
        month_high = hist_1m['High'].max() if not hist_1m.empty else 0
        year_low = hist_1y['Low'].min() if not hist_1y.empty else 0
        year_high = hist_1y['High'].max() if not hist_1y.empty else 0

        company_name = info.get('longName', stock_symbol)
        sector = info.get('sector', 'Bilinmiyor')

        return {
            'type': 'HISSE',
            'symbol': stock_symbol,
            'name': company_name,
            'sector': sector,
            'current_price': current_price,
            'daily': (daily_change, daily_change_percent),
            'weekly': (weekly_change, weekly_change_percent),
            'monthly': (monthly_change, monthly_change_percent),
            'three_month': (three_month_change, three_month_change_percent),
            'six_month': (six_month_change, six_month_change_percent),
            'month_low': month_low,
            'month_high': month_high,
            'year_low': year_low,
            'year_high': year_high,
            'hist_1d': hist_1d,
            'hist_1w': hist_1w,
            'hist_1m': hist_1m,
            'hist_3m': hist_3m,
            'hist_6m': hist_6m,
            'hist_1y': hist_1y,
            'last_update': datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        }

    except Exception as e:
        print(f"{Fore.RED}Hisse bilgisi alınırken hata: {str(e)}")
        return None


def get_asset_info(symbol):
    """
    Otomatik olarak hisse veya fon bilgisini getir
    """
    asset_type = detect_asset_type(symbol)

    if asset_type == "BIST100":
        get_bist100_list()
        return None

    # Önce hisse olarak dene
    stock_info = get_stock_info(symbol)
    if stock_info:
        return stock_info

    # Hisse bulunamazsa fon olarak dene
    fund_info = get_fund_info(symbol)
    if fund_info:
        return fund_info

    # Hiçbiri bulunamazsa
    print(f"{Fore.RED}Veri bulunamadı: {symbol}")
    return None


def plot_fund_charts(info):
    """
    Fonlar için özel grafikler
    """
    if not info:
        return

    fig = plt.figure(figsize=(16, 10))
    fig.suptitle(f"{info['name']} ({info['symbol']}) - Fon Performansı",
                 fontsize=16, fontweight='bold')

    # 1. Aylık grafik
    ax1 = plt.subplot(2, 3, 1)
    if not info['hist_1m'].empty:
        info['hist_1m']['Close'].plot(ax=ax1, color='blue', linewidth=2)
        ax1.fill_between(info['hist_1m'].index, info['hist_1m']['Low'],
                         info['hist_1m']['High'], alpha=0.2, color='gray')
        ax1.set_title('Aylık Performans', fontsize=12)
        ax1.set_ylabel('Fiyat (TL)')
        ax1.grid(True, alpha=0.3)

    # 2. 3 Aylık grafik
    ax2 = plt.subplot(2, 3, 2)
    if not info['hist_3m'].empty:
        info['hist_3m']['Close'].plot(ax=ax2, color='green', linewidth=2)
        ax2.set_title('3 Aylık Performans', fontsize=12)
        ax2.set_ylabel('Fiyat (TL)')
        ax2.grid(True, alpha=0.3)

    # 3. 6 Aylık grafik
    ax3 = plt.subplot(2, 3, 3)
    if not info['hist_6m'].empty:
        info['hist_6m']['Close'].plot(ax=ax3, color='orange', linewidth=2)
        ax3.set_title('6 Aylık Performans', fontsize=12)
        ax3.set_ylabel('Fiyat (TL)')
        ax3.grid(True, alpha=0.3)

    # 4. Yıllık grafik
    ax4 = plt.subplot(2, 3, 4)
    if not info['hist_1y'].empty:
        info['hist_1y']['Close'].plot(ax=ax4, color='red', linewidth=2)
        ax4.set_title('Yıllık Performans', fontsize=12)
        ax4.set_ylabel('Fiyat (TL)')
        ax4.grid(True, alpha=0.3)

    # 5. Getiri karşılaştırması (baz alınan endeks yoksa sadece fon)
    ax5 = plt.subplot(2, 3, 5)
    if not info['hist_1y'].empty:
        # Normalize edilmiş getiri (başlangıç=100)
        normalized = (info['hist_1y']['Close'] / info['hist_1y']['Close'].iloc[0]) * 100
        normalized.plot(ax=ax5, color='purple', linewidth=2, label='Fon')
        ax5.set_title('Normalize Edilmiş Getiri (Başlangıç=100)', fontsize=12)
        ax5.set_ylabel('Değer')
        ax5.legend()
        ax5.grid(True, alpha=0.3)

    # 6. Hacim grafiği
    ax6 = plt.subplot(2, 3, 6)
    if not info['hist_1m'].empty and 'Volume' in info['hist_1m'].columns:
        ax6.bar(info['hist_1m'].index, info['hist_1m']['Volume'],
                color='skyblue', alpha=0.6)
        ax6.set_title('Aylık İşlem Hacmi', fontsize=12)
        ax6.set_ylabel('Hacim')
        ax6.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def display_info(info):
    """
    Hisse veya fon bilgilerini görüntüle
    """
    if not info:
        return

    # Başlık rengi
    if info['type'] == 'FON':
        title_color = Fore.MAGENTA
        type_text = "📊 YATIRIM FONU"
    else:
        title_color = Fore.CYAN
        type_text = "📈 HİSSE SENEDİ"

    print(f"\n{title_color}{'=' * 80}{Style.RESET_ALL}")
    print(f"{title_color}{type_text}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{info['name']} ({info['symbol']}){Style.RESET_ALL}")
    if info['type'] == 'HISSE' and 'sector' in info:
        print(f"{Fore.CYAN}Sektör: {info['sector']}{Style.RESET_ALL}")
    elif info['type'] == 'FON' and 'fund_type' in info:
        print(f"{Fore.CYAN}Fon Tipi: {info['fund_type']}{Style.RESET_ALL}")
    print(f"{title_color}{'=' * 80}{Style.RESET_ALL}")

    # Ana tablo
    table_data = [
        ["💰 Güncel Fiyat", f"{info['current_price']:.4f} ₺"],
        ["📊 Günlük Değişim", format_change(*info['daily'])],
        ["📈 Haftalık Değişim", format_change(*info['weekly'])],
        ["📉 Aylık Değişim", format_change(*info['monthly'])],
        ["📊 3 Aylık Değişim", format_change(*info['three_month'])],
    ]

    # 6 aylık değişim varsa ekle
    if 'six_month' in info:
        table_data.append(["📊 6 Aylık Değişim", format_change(*info['six_month'])])

    # Ek bilgiler
    table_data.extend([
        ["📉 Son 1 Ay En Düşük", f"{info['month_low']:.4f} ₺"],
        ["📈 Son 1 Ay En Yüksek", f"{info['month_high']:.4f} ₺"],
        ["📊 Son 1 Yıl En Düşük", f"{info['year_low']:.4f} ₺"],
        ["📈 Son 1 Yıl En Yüksek", f"{info['year_high']:.4f} ₺"],
    ])

    print(tabulate(table_data, headers=["Metrik", "Değer"], tablefmt="grid", stralign="left"))
    print(f"{title_color}{'=' * 80}{Style.RESET_ALL}")
    print(f"🕐 Son Güncelleme: {info['last_update']}")


def format_change(change, percent):
    """Değişimi formatla ve renklendir"""
    if change > 0:
        return f"{Fore.GREEN}▲ {change:+.4f} ₺ (%{percent:+.2f}){Style.RESET_ALL}"
    elif change < 0:
        return f"{Fore.RED}▼ {change:+.4f} ₺ (%{percent:+.2f}){Style.RESET_ALL}"
    else:
        return f"{Fore.YELLOW}● {change:.4f} ₺ (%0.00){Style.RESET_ALL}"


def main():
    """Ana program"""
    print(f"{Fore.CYAN}🔴 BIST 100 ve Fon Takip Uygulaması 🔴{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Örnek hisse kodları: THYAO, GARAN, AKBNK, EREGL{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Örnek fon kodları: AFA, TTE, İJH, AZNVD, TURKSS{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Komutlar: '100'=BIST 100 Listesi, 'q'=Çıkış, 'g'=Grafik Göster{Style.RESET_ALL}\n")

    last_info = None

    while True:
        try:
            command = input(f"{Fore.GREEN}🔍 Sembol veya komut girin: {Style.RESET_ALL}").strip()

            if command.lower() == 'q':
                print(f"{Fore.YELLOW}Uygulamadan çıkılıyor...{Style.RESET_ALL}")
                break

            if command.lower() == 'g' and last_info:
                print(f"{Fore.YELLOW}Grafikler hazırlanıyor...{Style.RESET_ALL}")
                if last_info['type'] == 'FON':
                    plot_fund_charts(last_info)
                else:
                    # Hisse grafikleri için önceki kod
                    from matplotlib import pyplot as plt
                    # Hisse grafik fonksiyonunu çağır (önceki kodda vardı)
                    print(f"{Fore.YELLOW}Hisse grafikleri gösteriliyor...{Style.RESET_ALL}")
                    # plot_stock_charts(last_info) - önceki fonksiyon
                continue
            elif command.lower() == 'g':
                print(f"{Fore.RED}Önce bir sembol sorgulayın!{Style.RESET_ALL}")
                continue

            if not command:
                print(f"{Fore.RED}Lütfen bir sembol girin!{Style.RESET_ALL}")
                continue

            print(f"{Fore.YELLOW}Veriler alınıyor...{Style.RESET_ALL}")

            info = get_asset_info(command)

            if info:
                last_info = info
                display_info(info)
                print(f"\n{Fore.CYAN}📊 Grafikleri görmek için 'g' yazın{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Uygulamadan çıkılıyor...{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"{Fore.RED}Beklenmeyen hata: {str(e)}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()