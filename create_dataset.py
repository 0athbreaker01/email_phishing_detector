import pandas as pd


def create_email_dataset():
 

    phishing_emails = [
        "Urgent action required: your account has been suspended. Click here to verify your details immediately.",
        "Security Alert: Suspicious activity detected on your account. Verify your identity immediately.",
        "Your PayPal account has been limited. Click here to restore full access within 48 hours.",
        "Bank Alert: Unusual activity detected. Click here to secure your account immediately.",
        "Your Amazon account has been compromised. Update your password now to prevent unauthorized access.",
        "Apple ID Security Alert: Your account was accessed from an unknown device. Verify now to secure it.",
        "Microsoft Account Alert: We've detected suspicious sign-in activity. Confirm your identity immediately.",
        "Gmail Security Notice: Your account will be deactivated unless you verify your credentials now.",
        "Facebook Security Team: Your account has been temporarily locked. Click here to restore access.",
        "Instagram Alert: Someone tried to log into your account. Secure it now by clicking here.",
        "Twitter Security: Unusual login detected from Russia. Secure your account immediately.",
        "LinkedIn Warning: Your profile has been flagged for suspicious activity. Verify to restore access.",
        "Dropbox Alert: Your account shows signs of unauthorized access. Change password now.",
        "Spotify Security: Someone is using your account in another country. Secure it immediately.",
        "Netflix Account Alert: Suspicious activity detected. Verify your account to continue watching.",
        # Fake prizes/lottery scams
        "You have won a prize of $10,000! Claim it now at fakelink.com before it expires.",
        "CONGRATULATIONS! You've been selected for a special offer. Click here to claim your reward.",
        "You have won the lottery! Claim your $50,000 prize at winner-lottery.fake-site.com",
        "Lucky Winner! You've won $25,000 in our daily sweepstakes. Click here to collect your prize.",
        "WINNER ALERT: You've been chosen to receive a $1,000 gift card. Claim it within 24 hours.",
        "Congratulations! You've won a brand new iPhone 15. Click here to claim your free device now.",
        "You're our 1000th visitor today! You've won a $500 Amazon gift card. Click to claim.",
        "URGENT: Your lottery ticket has won $75,000! Click here before the deadline expires.",
        "Prize Alert: You've won a luxury vacation package worth $10,000. Claim it here immediately.",
        "BREAKING: You've been selected for a cash prize of $5,000. Verify your details to receive it.",
        "Mega Millions Winner: You've won $100,000! Claim your prize before it expires tomorrow.",
        "Sweepstakes Alert: You're the grand prize winner of $50,000 cash. Collect now.",
        "Contest Winner: Your entry has won a Tesla Model 3. Click here to arrange delivery.",
        "Lucky Day: You've won $15,000 in our random drawing. Claim within 48 hours.",
        "Publisher's Clearing House: You've won our $250,000 grand prize. Claim immediately.",
        # Password/account expiration scams
        "Your password for SecureBank expires in 24 hours. Update it now to avoid account closure.",
        "Urgent: Your email account will be deleted in 24 hours. Verify your account to prevent deletion.",
        "Password Expiry Notice: Your account password expires today. Update it now to maintain access.",
        "Account Maintenance: Your online banking password will expire in 6 hours. Renew it immediately.",
        "System Update Required: Your account needs verification within 12 hours or it will be suspended.",
        "Email Service Alert: Your mailbox is 99% full. Upgrade now or lose all your emails.",
        "Cloud Storage Warning: Your account will be terminated in 48 hours. Verify to keep your files.",
        "Security Update: Your account requires immediate password reset for continued access.",
        "Service Interruption Notice: Update your account details now to avoid service suspension.",
        "Account Verification Needed: Your profile will be deleted unless verified within 24 hours.",
        "Critical Alert: Your account expires at midnight. Renew now to avoid data loss.",
        "Maintenance Window: Your account will be locked unless you update credentials today.",
        "Security Patch: Your account needs immediate update to prevent unauthorized access.",
        "Account Cleanup: Inactive accounts will be deleted. Verify yours to keep it active.",
        "System Migration: Update your account info or lose access permanently.",
        # Money transfer/payment scams
        "You have received a money transfer of $5,000. Click here to accept the payment.",
        "Wire Transfer Alert: $15,000 has been sent to your account. Confirm receipt to access funds.",
        "Payment Notification: You have received $3,500. Click here to transfer to your bank account.",
        "Money Transfer Pending: $8,000 awaits your confirmation. Accept the transfer immediately.",
        "International Payment: You've received $12,000 from overseas. Verify to complete the transfer.",
        "Inheritance Notice: You've inherited $250,000. Contact us immediately to claim your funds.",
        "Business Partnership: Investor wants to transfer $50,000 to your account. Respond urgently.",
        "Compensation Payment: You're entitled to $7,500 compensation. Click here to claim it now.",
        "Refund Processing: Your $2,000 refund is ready. Provide account details to receive payment.",
        "Loan Approval: You've been pre-approved for $20,000. Accept the offer within 24 hours.",
        "Foreign Investment: Nigerian prince wants to share $10 million fortune with you.",
        "Estate Settlement: You're beneficiary of $500,000 estate. Contact lawyer immediately.",
        "Insurance Payout: Your claim has been approved for $75,000. Accept payment now.",
        "Legal Settlement: You're entitled to $25,000 class action settlement. Claim today.",
        "Trust Fund: Mysterious benefactor left you $100,000. Contact us to receive funds.",
        # Tax/government scams
        "IRS Tax Refund: You are eligible for a $2,500 refund. Click here to claim it today.",
        "Tax Alert: You owe $1,200 in back taxes. Pay immediately to avoid legal action.",
        "Government Grant: You qualify for a $5,000 federal grant. Apply now before funds run out.",
        "Social Security Administration: Your benefits will be suspended unless you verify your SSN.",
        "IRS Audit Notice: Your tax return has been flagged. Respond within 72 hours to avoid penalties.",
        "Treasury Department: You have unclaimed funds of $3,000. Claim them before they're forfeited.",
        "Medicare Update: Your coverage will be cancelled unless you update your information now.",
        "Stimulus Payment: You're eligible for an additional $1,400 payment. Claim it immediately.",
        "Tax Court Summons: You must appear in court unless you settle your debt of $2,800 today.",
        "Federal Grant Notification: You've been awarded $8,000. Accept the grant within 48 hours.",
        "IRS Criminal Investigation: You're under investigation for tax fraud. Call immediately.",
        "Social Security Suspension: Your number has been suspended due to illegal activity.",
        "Government Audit: Your assets will be frozen unless you respond within 6 hours.",
        "Federal Tax Lien: Your property will be seized unless you pay $5,000 today.",
        "IRS Warrant: There's a warrant for your arrest. Call this number to resolve.",
        # Fake charges/billing scams
        "Your credit card has been charged $499. If this was not you, click here to dispute.",
        "Final notice: Your subscription will be cancelled unless you update your payment information now.",
        "Netflix Billing: Your subscription will be cancelled unless you update payment info now.",
        "Amazon Prime: Your membership fee of $99 could not be processed. Update your card details.",
        "Apple iTunes: You've been charged $89.99 for app purchases. Dispute if unauthorized.",
        "Microsoft Office: Your subscription has expired. Renew now for $79 or lose access.",
        "Norton Antivirus: Auto-renewal of $159.99 processed. Cancel within 24 hours if unwanted.",
        "PayPal Payment: $299 sent to unknown recipient. Secure your account immediately.",
        "Credit Card Alert: Unusual charge of $1,299 detected. Verify this transaction now.",
        "Bank Notice: $750 withdrawal attempted from ATM in foreign country. Confirm if authorized.",
        "Subscription Alert: $49.99 charged for premium service. Cancel if you didn't authorize this.",
        "Walmart Purchase: $899 charged to your card for electronics. Dispute if not yours.",
        "Best Buy Transaction: $1,200 charged for laptop purchase. Contact us if unauthorized.",
        "Target Purchase Alert: $650 charged to your account. Click here to dispute charge.",
        "Gas Station Charge: $300 fuel purchase in different state. Verify if this was you.",
        # Tech support/virus scams
        "Computer Virus Alert: Your PC is infected with 47 viruses. Download our cleaner immediately.",
        "Microsoft Support: Your Windows license has expired. Renew now or lose access to your files.",
        "Apple Support: Your Mac has been compromised. Call us immediately at this number.",
        "Google Security: Your Chrome browser has been hacked. Install our security patch now.",
        "Norton Alert: Your computer is at risk. Purchase our antivirus software immediately.",
        "McAfee Warning: 12 threats detected on your device. Buy our protection software now.",
        "Windows Defender: Critical security update required. Download and install immediately.",
        "Tech Support: Your IP address has been compromised. Contact us within 1 hour.",
        "System Alert: Your computer will be locked in 5 minutes unless you call this number.",
        "Adobe Flash: Critical security update available. Install now to protect your system.",
        "Java Security: Your computer is vulnerable. Update Java immediately to stay protected.",
        "Firefox Alert: Your browser has been infected. Download our security tool now.",
        "Internet Provider: Your connection is compromised. Install our security software.",
        "Router Security: Your WiFi has been hacked. Call us to secure your network.",
        "System Scan: 25 errors found on your computer. Fix them now with our software.",
        # Job/employment scams
        "Congratulations! You've been hired for a $5,000/week work-from-home job. Start immediately.",
        "Easy Money: Earn $200/hour working from home. No experience needed. Apply now.",
        "Job Offer: We need you to process payments. Earn $50 per transaction.",
        "Employment Opportunity: Make $300/day stuffing envelopes at home.",
        "Urgent Hiring: Personal assistant needed. $2,000/week salary. Reply immediately.",
        "Data Entry Position: Work from home earning $150/hour. No experience required.",
        "Customer Service Rep: $25/hour remote work. Flexible schedule. Start today.",
        "Survey Taker: Earn $100 per survey completed. Work when you want.",
        "Secret Shopper: Get paid $200 per assignment plus keep purchases.",
        "Online Tutor: Earn $75/hour teaching from home. No degree required.",
        # Cryptocurrency/investment scams
        "Bitcoin Investment: Double your money in 7 days. Minimum investment $500.",
        "Crypto Alert: Your wallet has been compromised. Secure it now with our service.",
        "Trading Opportunity: Guaranteed 500% returns on forex trading. Invest now.",
        "NFT Collection: Exclusive drop worth $10,000. Buy now before prices skyrocket.",
        "Stock Tip: This penny stock will increase 1000% tomorrow. Buy now.",
    ]

    legitimate_emails = [
        # Business communications
        "Here is the meeting summary from yesterday. Please review the action items and let me know if you have questions.",
        "Project update for Q3: We are on track to meet our deadlines. The next milestone is scheduled for next week.",
        "Can we schedule a call for next week to discuss the upcoming project requirements?",
        "The quarterly financial report is attached. Please review and provide your feedback by Friday.",
        "Thank you for attending our webinar yesterday. The presentation slides are attached for your reference.",
        "Reminder: The team meeting is scheduled for tomorrow at 2 PM in the conference room.",
        "I've completed the code review for your pull request. Everything looks good, approved for merge.",
        "The conference call with the client went well. I'll send you the notes and next steps shortly.",
        "Please find the updated project timeline attached. Let me know if you need any clarifications.",
        "The budget proposal has been approved by management. We can proceed with the implementation.",
        "I wanted to follow up on our discussion about the new marketing strategy.",
        "The training materials for next week's workshop are now available on the shared drive.",
        "Our Q4 goals have been finalized. I'll share them with the team in tomorrow's meeting.",
        "The client feedback on our proposal was positive. They want to move forward with phase 2.",
        "I've scheduled a review meeting for the project deliverables next Thursday at 3 PM.",
        # Order confirmations and shipping
        "Your order #12345 has shipped and will arrive within 3-5 business days. Thank you for your purchase.",
        "Order confirmation: Your purchase of office supplies has been processed and will ship today.",
        "Shipping notification: Your package is on its way and will be delivered by Friday.",
        "Your order has been received and is being prepared for shipment.",
        "Delivery confirmation: Your package was successfully delivered at 2:30 PM today.",
        "Return processed: Your refund of $89.99 will appear on your statement within 3-5 business days.",
        "Your backorder item is now in stock and will ship within 24 hours.",
        "Package delayed: Your shipment will arrive 1 day later than expected due to weather.",
        "Your subscription box has shipped and includes tracking number 1Z999AA1234567890.",
        "Order update: One item in your order is temporarily out of stock but will ship separately.",
        "Your grocery delivery is confirmed for tomorrow between 2-4 PM.",
        "Prescription ready: Your medication is available for pickup at the pharmacy.",
        "Your custom order has been completed and is ready for delivery.",
        "Installation scheduled: Our technician will arrive Thursday between 10 AM and 2 PM.",
        "Service appointment confirmed for next Tuesday at 9 AM for your annual maintenance.",
        # Account and subscription updates
        "Your subscription renewal is due next month. You will receive an invoice via email shortly.",
        "Your monthly statement is now available in your online account. You can download it from the portal.",
        "Account update: Your new password has been successfully changed as requested.",
        "Your annual membership will expire on December 31st. Renewal options are available online.",
        "Statement ready: Your credit card statement for November is now available for download.",
        "Payment received: Thank you for your payment of $149.99. Your account is current.",
        "Your automatic backup service is working properly and last ran successfully yesterday.",
        "Security notice: You recently logged in from a new device. This is just a notification.",
        "Your cloud storage usage is at 75% capacity. Consider upgrading or cleaning up files.",
        "Profile updated: Your contact information has been successfully changed.",
        "Your warranty registration has been confirmed for your recent purchase.",
        "Billing cycle change: Your next statement will reflect the new billing date.",
        "Your loyalty points balance is 2,547 points, worth approximately $25 in rewards.",
        "Two-factor authentication has been enabled on your account for added security.",
        "Your account preferences have been updated according to your recent changes.",
        # System and maintenance notices
        "The server maintenance is scheduled for this weekend. Please save your work before Friday evening.",
        "System update completed successfully. All services are now fully operational.",
        "Scheduled maintenance window tonight from 11 PM to 3 AM. Expect brief service interruptions.",
        "Software update available: Version 2.1.4 includes bug fixes and security improvements.",
        "Database backup completed successfully last night. All data is secure.",
        "Network upgrade scheduled for next weekend. Internet service may be intermittent.",
        "Security patch applied to all systems. No action required on your part.",
        "Server migration completed. All services have been restored to normal operation.",
        "Backup verification successful. Your data protection is working properly.",
        "System performance improvements deployed. You may notice faster response times.",
        "Firewall update completed. Your security settings remain unchanged.",
        "Email server maintenance finished early. All functionality has been restored.",
        "Cloud service upgrade deployed. New features are now available in your dashboard.",
        "Load balancing optimization completed. Service reliability has been improved.",
        "Security monitoring system updated with latest threat detection capabilities.",
        # Training and HR communications
        "The training session for new employees is scheduled for next Tuesday. Please confirm your attendance.",
        "Employee handbook updates are now available on the HR portal.",
        "Annual performance reviews will begin next month. Schedule your meeting with your manager.",
        "Open enrollment for health benefits starts Monday and ends on the 30th.",
        "Mandatory safety training is scheduled for all staff on Wednesday at 10 AM.",
        "Your vacation request for next week has been approved by your supervisor.",
        "New employee orientation will be held every first Monday of the month.",
        "Updated company policies are available for review on the intranet.",
        "Team building event scheduled for Friday afternoon in the main conference room.",
        "Benefits enrollment deadline is approaching. Complete your selections by Friday.",
        "Professional development workshop: Advanced Excel training available next month.",
        "Work-from-home policy updates have been posted to the employee portal.",
        "Lunch and learn session: Cybersecurity awareness training on Thursday.",
        "Annual company picnic is scheduled for Saturday, June 15th at Central Park.",
        "New hire welcome packet is ready for pickup from HR.",
        # Educational and informational
        "Course enrollment is now open for the spring semester. Register by January 15th.",
        "Library notification: Your reserved book is now available for pickup.",
        "Tuition payment deadline is approaching. Please submit payment by the due date.",
        "Your transcript request has been processed and will be mailed within 5 business days.",
        "Registration confirmation: You are enrolled in Biology 101 for the fall semester.",
        "Scholarship application deadline is March 1st. All materials must be submitted online.",
        "Final exam schedule has been posted. Check your student portal for details.",
        "Grade report: Your midterm grades are now available in the student information system.",
        "Research opportunity available in the psychology department. Apply by next Friday.",
        "Study abroad program applications are due February 15th for summer programs.",
        "Campus housing applications for next year open on March 1st.",
        "Career fair scheduled for April 10th in the student center. All majors welcome.",
        "Laboratory safety training required for all science students before lab access.",
        "Academic advisors are available for course planning meetings this week.",
        "Commencement ceremony details will be mailed to graduating students next month.",
        # Healthcare and medical
        "Appointment reminder: Your annual checkup is scheduled for next Tuesday at 10 AM.",
        "Lab results are ready. Please call our office to schedule a follow-up appointment.",
        "Your prescription refill is ready for pickup at the pharmacy.",
        "Immunization records have been updated in your patient portal.",
        "Insurance claim processed: Your recent visit has been approved for coverage.",
        "Appointment confirmed: Physical therapy session on Thursday at 2 PM.",
        "Your dental cleaning is scheduled for next month. We'll send a reminder closer to the date.",
        "Blood work completed. Results show all values within normal ranges.",
        "Medication reminder: Time to refill your monthly prescription.",
        "Flu shots are now available. Schedule your appointment online or by phone.",
        "Your MRI scan is scheduled for Friday at 9 AM. Please arrive 30 minutes early.",
        "Specialist referral approved. Dr. Smith's office will contact you to schedule.",
        "Annual physical exam results show excellent health. Keep up the good work.",
        "Vision screening completed. No changes needed to your current prescription.",
        "Telehealth appointment available. Video consultation scheduled for Monday.",
        # Financial and banking
        "Your direct deposit has been processed and funds are now available in your account.",
        "Monthly statement summary: Account balance as of statement date is $2,847.33.",
        "Automatic payment scheduled for your mortgage will process on the 15th.",
        "Your loan application has been approved. Closing is scheduled for next Friday.",
        "Investment portfolio summary: Your account gained 3.2% this quarter.",
        "Tax documents are now available for download from your online banking portal.",
        "Credit score update: Your score has improved by 12 points this month.",
        "Savings goal achieved: You've reached 50% of your target for the year.",
        "Mobile deposit processed successfully. Funds will be available tomorrow morning.",
        "Account alert: Low balance notification. Current balance is below your set threshold.",
        "Payment confirmation: Your credit card payment of $245.67 has been received.",
        "New feature: Mobile check deposit is now available in our banking app.",
        "Certificate of deposit has matured. Please contact us to discuss renewal options.",
        "Foreign transaction notice: International purchase processed without issues.",
        "Your debit card order has been processed and will arrive in 7-10 business days.",
    ]

    phishing_df = pd.DataFrame(
        {
            "text": phishing_emails,
            "label": [1] * len(phishing_emails),  
        }
    )

    legitimate_df = pd.DataFrame(
        {
            "text": legitimate_emails,
            "label": [0] * len(legitimate_emails),  
        }
    )

    combined_df = pd.concat([phishing_df, legitimate_df], ignore_index=True)

    combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

    return combined_df


def main():
    
    print("Creating comprehensive email dataset...")

    email_dataset = create_email_dataset()

    print(f"Total emails created: {len(email_dataset)}")
    print(f"Phishing emails: {sum(email_dataset['label'])}")
    print(f"Legitimate emails: {len(email_dataset) - sum(email_dataset['label'])}")

    email_dataset.to_csv("emails.csv", index=False)
    print("Expanded dataset saved to 'emails.csv'")

    print("\nFirst 5 rows of the dataset:")
    print(email_dataset.head())

    print(f"\nDataset Statistics:")
    print(f"- Total samples: {len(email_dataset)}")
    print(
        f"- Phishing samples: {sum(email_dataset['label'])} ({sum(email_dataset['label']) / len(email_dataset) * 100:.1f}%)"
    )
    print(
        f"- Legitimate samples: {len(email_dataset) - sum(email_dataset['label'])} ({(len(email_dataset) - sum(email_dataset['label'])) / len(email_dataset) * 100:.1f}%)"
    )
    print(
        f"- Average email length: {email_dataset['text'].str.len().mean():.1f} characters"
    )


if __name__ == "__main__":
    main()


