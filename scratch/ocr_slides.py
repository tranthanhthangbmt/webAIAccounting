import fitz
import os
import subprocess

pdf_path = r"d:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Môn TTNT cho kế toán_2026\webAIAccounting\video\Day04_Extra\videos\P1_lý thuyết_Generative_AI_trong_Kế_toán_và_Kiểm_toán\slide.pdf"
doc = fitz.open(pdf_path)
print("Total pages:", len(doc))

ps_script = """
Add-Type -AssemblyName System.Drawing
[Windows.Globalization.Language, Windows.Globalization, ContentType=WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType=WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation, ContentType=WindowsRuntime] | Out-Null

$asyncHelper = @'
using System;
using System.IO;
using System.Threading.Tasks;
using Windows.Graphics.Imaging;
using Windows.Media.Ocr;
using Windows.Storage.Streams;

public class WinOcrHelper {
    public static string RecognizeFile(string filePath) {
        return RecognizeAsync(filePath).GetAwaiter().GetResult();
    }
    private static async Task<string> RecognizeAsync(string filePath) {
        var fileBytes = File.ReadAllBytes(filePath);
        using (var stream = new InMemoryRandomAccessStream()) {
            using (var writer = new DataWriter(stream)) {
                writer.WriteBytes(fileBytes);
                await writer.StoreAsync();
                await writer.FlushAsync();
            }
            stream.Seek(0);
            var decoder = await BitmapDecoder.CreateAsync(stream);
            var softwareBitmap = await decoder.GetSoftwareBitmapAsync();
            var lang = new Windows.Globalization.Language("en-US");
            var engine = OcrEngine.TryCreateFromLanguage(lang);
            var result = await engine.RecognizeAsync(softwareBitmap);
            return result.Text;
        }
    }
}
'@

Add-Type -TypeDefinition $asyncHelper

for ($i=1; $i -le 15; $i++) {
    $fn = "temp_page_$i.png"
    if (Test-Path $fn) {
        $txt = [WinOcrHelper]::RecognizeFile((Resolve-Path $fn).Path)
        Write-Output ("=== SLIDE " + $i + " ===")
        Write-Output $txt
        Remove-Item $fn -Force
    }
}
"""

with open("scratch/run_ocr.ps1", "w", encoding="utf-8") as f:
    f.write(ps_script)

for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)
    pix.save(f"temp_page_{i+1}.png")

print("Images saved, running OCR...")
res = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "scratch/run_ocr.ps1"], capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout)
if res.stderr:
    print("ERR:", res.stderr[:500])

