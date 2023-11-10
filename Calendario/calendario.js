
const actualYear = 2024
const locale = 'es'

const intlForMonths = new Intl.DateTimeFormat(locale, { month: 'long' })
const months = [...Array(12).keys()]

const intlForWeeks = new Intl.DateTimeFormat(locale, { weekday: 'short' })
const weekDays = [...Array(7).keys()].map((dayIndex) =>
  intlForWeeks.format(new Date(2021, 2, dayIndex + 1))
)

const calendar = months.map((monthIndex) => {
  const monthName = intlForMonths.format(new Date(actualYear, monthIndex))
  const nextMonthIndex = (monthIndex + 1) % 12
  const daysOfMonth = new Date(actualYear, nextMonthIndex, 0).getDate()
  const startsOn = new Date(actualYear, monthIndex, 1).getDay()

  return {
    daysOfMonth,
    monthName,
    startsOn
  }
})

const html = `<div class="month-container">` + calendar
  .map(({ daysOfMonth, monthName, startsOn }) => {
    const days = [...Array(daysOfMonth).keys()]
    const firstDayAttributes = `class='first-day' style='--first-day-start: ${startsOn}'`
    const htmlDaysName = weekDays
      .map((dayName) => `<li class='day-name'>${dayName}</li>`)
      .join('')
    const htmlDays = days
      .map(
        (day, index) =>
          `<li ${index === 0 ? firstDayAttributes : ''}>${day + 1}</li>`
      )
      .join('')
    return  `<div class="month"><h2>${monthName} ${actualYear}</h2><ol>${htmlDaysName}${htmlDays}</ol></div>`
  })
  .join('')

  document.getElementById('calendar').innerHTML = html;