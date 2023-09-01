import { StyleSheet, Image } from "react-native";

export default function ImageViewer ({placeholderImageSource, selectedImage}) {

    const imageSource = selectedImage ? {uri: selectedImage} : placeholderImageSource;

    return (
        <Image source={imageSource} style={styles.image}/>
    );
}

const styles = StyleSheet.create({
    image: {
        width: 360,
        height: 280,
        borderRadius: 18,
      },
});