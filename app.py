from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

# List of blog post URLs
blog_urls = [
    "https://www.linkedin.com/pulse/building-better-cloud-solutions-vasanthabalaji-k/?trackingId=WktFT6RxRwuhTRiR0r0qIA%3D%3D",
    "https://www.linkedin.com/pulse/technology-stacks-vasanthabalaji-k/?trackingId=WktFT6RxRwuhTRiR0r0qIA%3D%3D",
    "https://medium.com/@vasanthabalaji/python-intermediate-c231236fdbb5",
    "https://medium.com/@vasanthabalaji/start-from-here-4edff558fd22",
    "https://medium.com/@vasanthabalaji/exploring-ai-and-ml-in-computer-vision-3a4d65f2a1f1",
    "https://medium.com/@vasanthabalaji/oracle-virtual-box-instalation-e2e8a8918f2",
    "https://medium.com/@vasanthabalaji/get-start-linux-450b714873b",
    "https://medium.com/@vasanthabalaji/snort-on-ubuntu-3d865834c768",
    "https://medium.com/@vasanthabalaji/nessus-on-kali-linux-9f38e66eb085",
    "https://medium.com/@vasanthabalaji/capture-icmp-ssh-traffic-80e39213c409",
    "https://medium.com/@vasanthabalaji/guide-to-building-your-own-ott-platform-with-emby-on-aws-f7445517a76d",
    "https://medium.com/@vasanthabalaji/flaws-ctf-677726fa14b8",
    "https://medium.com/@vasanthabalaji/back-on-track-in-aws-saaco3-99ffd4e09730",
    "https://medium.com/@vasanthabalaji/saa-c03-whitepapers-and-aws-services-to-master-fbf54c96647e",
    "https://medium.com/@vasanthabalaji/aws-well-architected-framework-6-pillars-explained-83af8e29ce0d",
    "https://medium.com/@vasanthabalaji/aws-cloud-adoption-framework-ad11d3623150",
    "https://medium.com/@vasanthabalaji/disaster-recovery-of-on-premises-applications-to-aws-52432fb23fc1",
    "https://medium.com/@vasanthabalaji/security-best-practices-for-manufacturing-operations-technology-b3678787781d",
    "https://medium.com/@vasanthabalaji/aws-core-services-8b0d9842d55c",
    "https://medium.com/@vasanthabalaji/ec2-3582e5445731",
    "https://medium.com/@vasanthabalaji/list/aws-services-f193ec57a939",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_blog', methods=['POST'])
def show_blog():
    clicked_image = request.form.get('image_clicked', None)
    print(f"Clicked Image: {clicked_image}")  # For debugging purposes

    if clicked_image == 'Mr.Cloudexplorer_logo.png':
        if blog_urls:
            # Randomly select one blog link
            selected_blog_link = random.choice(blog_urls)

            # Redirect to the selected blog link
            return redirect(selected_blog_link)

    return "Invalid request"

if __name__ == '__main__':
    app.run(debug=True)
