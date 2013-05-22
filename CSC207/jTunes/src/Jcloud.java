import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.URL;
import java.util.List;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class Jcloud {
	// A Node that contains the information in XML regarding whether the
	// connection was successful.
	private static Node success;

	/**
	 * Create and returns a XML document from the given url address.
	 * 
	 * @param url
	 *            : String url address of the XML file.
	 * 
	 * @return Document: XML document in the given url.
	 * @return null: if the given url is incorrect.
	 */
	public static Document openURL(String url) {
		Document doc = null;
		try {
			// Open a new Document from the given url with the DocumentBuilder
			// created from Execution.
			doc = Execution.openXml().parse(new URL(url).openStream());
		} catch (SAXException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		// Put the document doc into a form that's accessible by build-in
		// methods
		doc.getDocumentElement().normalize();
		// Set success the node containing information regard to whether the
		// connection was successful.
		success = doc.getElementsByTagName("response").item(0);
		return doc;
	}

	/**
	 * create user in jCloud web service, indicate whether user account creation is successful or not.
	 * 
	 * @param url: s
	 * 
	 * @return boolean
	 */
	public static boolean createUser(String url) {
		openURL(url);
		boolean suc = Boolean.parseBoolean(success.getAttributes().item(0)
				.getNodeValue());
		System.out.println(success.getTextContent());
		return suc;
	}

	/**
	 * Add all the songs and its information from jCloud system to jCloudSongs
	 * list and return it.
	 * 
	 * @param jCloudSongs
	 *            : And empty List<String> that will be used to store all the
	 *            songs and its information in jCloud system.
	 * 
	 * @return jCloudSongs: A List<String> with all the songs and its
	 *         information in jCloud.
	 */
	public static List<String> listSongs(List<String> jCloudSongs) {
		Document doc = openURL("http://greywolf.cdf.toronto.edu:1337/pineapple/listSongs");
		// Get all the nodes of song.
		NodeList songs = doc.getElementsByTagName("song");
		String title;
		String artist;
		String sid;
		for (int i = 0; i < songs.getLength(); i++) {
			// Get the song's information from the node.
			artist = songs.item(i).getAttributes().item(0).getNodeValue()
					.trim();
			title = songs.item(i).getAttributes().item(1).getNodeValue().trim();
			sid = songs.item(i).getTextContent().trim();
			// store all information in a List<String>
			jCloudSongs.add(title);
			jCloudSongs.add(sid);
			jCloudSongs.add(artist);
		}
		return jCloudSongs;
	}

	/**
	 * Print out all the songs and its information in jCloud system to the user.
	 */
	public static void listSongs() {
		Document doc = openURL("http://greywolf.cdf.toronto.edu:1337/pineapple/listSongs");
		// Get all the nodes of song.
		NodeList songs = doc.getElementsByTagName("song");
		String title;
		String artist;
		for (int i = 0; i < songs.getLength(); i++) {
			// Get the song's information from the node.
			artist = songs.item(i).getAttributes().item(0).getNodeValue()
					.trim();
			title = songs.item(i).getAttributes().item(1).getNodeValue().trim();
			System.out.println(title + "\nBy: " + artist + "\n");
		}
	}

	/**
	 * Open the song file from the given url and copy every bits to a new file
	 * created in the current directory.
	 * 
	 * @param url
	 *            : String url address of the song file, and string.
	 * @param filename
	 *            : String name of the file which is going to be stored in
	 *            directory.
	 * 
	 * @return suc : Boolean that indicates whether or not the song is opened
	 *         correctly from the url.
	 */
	public static boolean getSong(String url, String filename) {
		Document doc = openURL(url);
		boolean suc = Boolean.parseBoolean(success.getAttributes().item(0)
				.getNodeValue());
		if (suc) {
			// Get all the hexadecimal bits from the song file.
			String rawData = doc.getElementsByTagName("rawdata").item(0)
					.getTextContent();
			// Calls hexToByte to decode and put the decoded binary bits in
			// byte[].
			byte[] byteData = hexToByte(rawData);
			OutputStream output;
			try {
				// Create a new file named by filename.
				output = new BufferedOutputStream(
						new FileOutputStream(filename));
				// Write all the binary bits to the file.
				output.write(byteData);
				output.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			String msg = success.getTextContent();
			// Print out error message if connection was unsuccessful.
			if (msg.contains("Song")) {
				System.out.println(msg);
			} else {
				System.out.println("Useremail or password given incorrect.");
			}
		}
		return suc;
	}

	/**
	 * Convert all the hexadecimal bits to binary bits and return them as
	 * byte[].
	 * 
	 * @param data
	 *            : String hexadecimal data that needs to be converted.
	 * 
	 * @return bin : Byte array that contains all the binary bits converted from
	 *         data.
	 */
	public static byte[] hexToByte(String data) {
		int len = data.length();
		// Use built-in functions to convert hexadecimal to binary digit
		byte[] bin = new byte[len / 2];
		for (int i = 0; i < len; i += 2) {
			bin[i / 2] = (byte) ((Character.digit(data.charAt(i), 16) << 4) + Character
					.digit(data.charAt(i + 1), 16));
		}
		return bin;
	}

	/**
	 * Open the given url, and return all the songIDs of the songs the user
	 * downloaded previously.
	 * 
	 * @param url
	 *            : String url address that contains the user infomation.
	 * @param downloadedSongs
	 *            : List<String> that will be used to store all the songID of
	 *            the songs the user had downloaded previuosly.
	 * 
	 * @return downloadedSongs : List<String> that contains all the songID of
	 *         the Songs user previously downloaded.
	 */
	public static List<String> listDownloadedSongs(String url,
			List<String> downloadedSongs) {
		Document doc = openURL(url);
		boolean suc = Boolean.parseBoolean(success.getAttributes().item(0)
				.getNodeValue());
		if (suc) {
			// Get all the song nodes.
			NodeList songId = doc.getElementsByTagName("song");
			for (int i = 0; i < songId.getLength(); i++) {
				// Get the songID from song nodes, and append it to
				// downloadedSongs
				downloadedSongs.add(songId.item(i).getTextContent().trim());
			}
		} else {
			System.out.println("Useremail or password given incorrect.");
		}
		return downloadedSongs;
	}

	/**
	 * Open the given url to varify whether the given user's email and user's
	 * password are correct.
	 * 
	 * @param url
	 *            : String url that contains the user's information.
	 * 
	 * @return suc : Boolean that indicates whether the connection of the given
	 *         url was successful.
	 */
	public static boolean listDownloadedSongs(String url) {
		openURL(url);
		// Get the information indicating whether or not the connection was
		// success.
		boolean suc = Boolean.parseBoolean(success.getAttributes().item(0)
				.getNodeValue());
		if (!suc) {
			System.out.println("Useremail or password given incorrect.");
		}
		return suc;
	}
}
