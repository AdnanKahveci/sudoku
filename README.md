# Sudoku Çözümleyici

Bu proje, Python ve Tkinter kullanarak bir Sudoku çözümleyici ve oluşturucu uygulaması geliştirir. Uygulama, ileriye dönük kontrol (forward checking) algoritması kullanarak Sudoku bulmacalarını çözmek için bir grafik kullanıcı arayüzü (GUI) sağlar. Kullanıcılar, otomatik olarak oluşturulan bir Sudoku bulmacasını çözebilir veya çözümün tamamını tek bir buton tıklamasıyla görebilirler.

## Özellikler

- **Sudoku Oluşturucu**: Otomatik olarak rastgele bir Sudoku tahtası oluşturur ve hücrelerin bazılarını boş bırakır.
- **Sudoku Çözümleyici**: İleriye dönük kontrol algoritması kullanarak Sudoku bulmacasını çözer.
- **Kullanıcı Dostu Arayüz**: Tkinter kullanılarak oluşturulmuş basit ve etkileşimli bir kullanıcı arayüzü.

## Gereksinimler

Bu proje, aşağıdaki Python kütüphanelerini gerektirir:

- `numpy`
- `tkinter`

Tkinter, genellikle Python ile birlikte gelir. Eğer yoksa, aşağıdaki komutla kurabilirsiniz:

```bash
pip install numpy
```
## Kurulum
Bu repoyu yerel makinenize klonlayın:
  ```bash
  git clone https://github.com/kullanici-adiniz/sudoku-cozumleyici.git
  ```
Gerekli kütüphaneleri yükleyin:
  ```bash
  pip install numpy
  ```
## Kullanım
Terminal veya komut istemcisinde projeyi çalıştırın:
  ```bash
  python sudoku_solver.py
  ```
Uygulama başlatıldığında, otomatik olarak oluşturulan bir Sudoku tahtası göreceksiniz.

"Çözümü Başlat" butonuna tıklayarak Sudoku'nun çözülmesini başlatabilirsiniz. Sudoku çözümü tamamlandığında, çözülen Sudoku tahtası ekranda gösterilecektir.

## Fonksiyonlar

- **is_valid(board, row, col, num)**: Belirtilen numarayı verilen satır, sütun ve 3x3 bölgesinde kontrol eder. Sudoku kurallarına göre geçerli olup olmadığını belirler.
- **find_empty(board)**: Sudoku tahtasında ilk boş hücreyi bulur. Boş hücre, çözülmesi gereken hücre anlamına gelir.
- **forward_checking(board)**: Her hücre için geçerli olası değerleri tutan bir sözlük oluşturur. Bu sözlük, ileriye dönük kontrol algoritmasının temelini oluşturur.
- **solve_sudoku_with_forward_checking(board)**: İleriye dönük kontrol algoritmasını kullanarak Sudoku bulmacasını çözer. Boş hücrelere numaralar yerleştirir ve çözüme ulaşmaya çalışır.
- **generate_sudoku()**: Rastgele bir Sudoku tahtası oluşturur ve belirli sayıda hücreyi boş bırakır. Bu boş hücreler, kullanıcı tarafından çözülmesi gereken kısımları temsil eder.
- **update_gui(board)**: GUI üzerindeki hücrelerin içeriğini günceller. Çözülen veya güncellenen tahtayı kullanıcıya gösterir.
- **start_solving()**: "Çözümü Başlat" butonuna tıklandığında çağrılır ve Sudoku çözme sürecini başlatır.

## GUI Bileşenleri

- **Tkinter**: GUI'nin oluşturulması için kullanılır.
- **tk.Entry**: Her hücre, bir `tk.Entry` bileşeni ile temsil edilir ve 9x9'luk bir ızgaraya yerleştirilir.
- **Çözümü Başlat Butonu**: Sudoku çözüm sürecini başlatan bir buton.

## Katkıda Bulunun

Eğer projeye katkıda bulunmak isterseniz, lütfen bir Pull Request (PR) gönderin veya bir Issue açın. Yeni özellikler, hata düzeltmeleri veya geliştirmeler her zaman memnuniyetle karşılanır!
