package com.mafia.game;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.ui.Label;
import com.badlogic.gdx.scenes.scene2d.ui.Table;
import com.badlogic.gdx.scenes.scene2d.ui.TextButton;
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener;
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.ScreenViewport;

public class MoneyScreen implements Screen {
    private final Mafia game;
    private Stage stage;
    private BitmapFont font;

    // Demo Bakiye Değişkeni
    private int cash = 150000;

    public MoneyScreen(Mafia game) {
        this.game = game;
        stage = new Stage(new ScreenViewport(), game.batch);

        // LibGDX'in varsayılan fontunu oluşturup biraz büyütüyoruz
        font = new BitmapFont();
        font.getData().setScale(1.5f);

        setupUI();
    }

    private void setupUI() {
        Table table = new Table();
        table.setFillParent(true); // Tabloyu tüm ekrana yay
        table.top().padTop(80); // Üstten boşluk bırak (Aşağıya çok inmesin)

        // Yazı Stilleri (Altın ve Beyaz)
        Label.LabelStyle titleStyle = new Label.LabelStyle(font, Color.GOLD);
        Label.LabelStyle normalStyle = new Label.LabelStyle(font, Color.WHITE);

        // Buton Stili (Koyu Gri arkaplan)
        TextButton.TextButtonStyle btnStyle = new TextButton.TextButtonStyle();
        btnStyle.font = font;
        btnStyle.up = createSolidBackground(Color.DARK_GRAY);
        btnStyle.down = createSolidBackground(Color.LIGHT_GRAY); // Tıklanınca açık gri olsun

        // Arayüz Elemanlarını Oluştur
        Label titleLabel = new Label("--- FINANS MERKEZI ---", titleStyle);
        final Label cashLabel = new Label("Nakit: $" + cash, normalStyle);

        TextButton collectBtn = new TextButton("Harac Topla (+$5000)", btnStyle);
        TextButton launderBtn = new TextButton("Para Akla (Yakinda)", btnStyle);

        // Haraç Topla Butonuna Tıklama Olayı
        collectBtn.addListener(new ClickListener() {
            @Override
            public void clicked(InputEvent event, float x, float y) {
                cash += 5000; // Parayı artır
                cashLabel.setText("Nakit: $" + cash); // Ekrandaki yazıyı güncelle
            }
        });

        // Elemanları Tabloya Ekle (Alt alta dizilmeleri için .row() kullanıyoruz)
        table.add(titleLabel).colspan(2).padBottom(30).row();
        table.add(cashLabel).colspan(2).padBottom(50).row();

        table.add(collectBtn).size(250, 60).pad(10);
        table.add(launderBtn).size(250, 60).pad(10);

        stage.addActor(table);
    }

    // Butonlar için kodla düz renkli arkaplan üreten yardımcı metod
    private TextureRegionDrawable createSolidBackground(Color color) {
        Pixmap pixmap = new Pixmap(1, 1, Pixmap.Format.RGBA8888);
        pixmap.setColor(color);
        pixmap.fill();
        Texture texture = new Texture(pixmap);
        pixmap.dispose();
        return new TextureRegionDrawable(texture);
    }

    @Override
    public void show() {
        // Bu sekmeye girildiğinde ekrandaki butonların tıklanabilmesi için
        game.inputMultiplexer.addProcessor(stage);
    }

    @Override
    public void hide() {
        // Başka sekmeye geçildiğinde bu sahnenin tıklamalarını durdur
        game.inputMultiplexer.removeProcessor(stage);
    }

    @Override
    public void render(float delta) {
        // Para sekmesi için paraya uygun KOYU YEŞİL bir arkaplan
        ScreenUtils.clear(0.05f, 0.2f, 0.1f, 1);

        stage.act(delta);
        stage.draw();
    }

    @Override
    public void resize(int width, int height) {
        stage.getViewport().update(width, height, true);
    }

    @Override public void pause() {}
    @Override public void resume() {}

    @Override
    public void dispose() {
        stage.dispose();
        font.dispose();
    }
}
